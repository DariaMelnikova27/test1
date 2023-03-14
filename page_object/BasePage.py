import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import logging
import time


class BasePage:
    """ Базовый класс с общими mетодами для всех страниц """
    url = "https://spb.ticketland.ru/"
    page_url = None

    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('example.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    logger.info('====== Started: {} ======'.format(int(time.time())))
    logger.info('====== Finished: {} ======'.format(int(time.time())))

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликаю по элементу {element}")
    def click(self, element):
        self.logger.info("Clicking element: {}".format(element))
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step("Ввожу {value} в элемент {element}")
    def _input(self, element, value):
        self.logger.info("Input {} in input {}".format(value, element))
        self.click(element)
        element.clear()
        element.send_keys(value)

    @allure.step("Жду элемент {locator}")
    def element(self, locator: tuple):
        self.logger.info("Check if element {} is present".format(locator))
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg, f"Не дождался видимости элемента {locator}")

    @allure.step("Нахожу элемент {locator}")
    def _find_element(self, locator):
        self.logger.info("Check if element {} is find".format(locator))
        try:
            return self.driver.find_elements(*locator)
        except TimeoutException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e.msg)

    @allure.step("Открываю страницу")
    def open_page(self, browser):
        self.logger.info("Opening url: {}".format(browser.url + self.page_url))
        browser.get(browser.url + self.page_url)
