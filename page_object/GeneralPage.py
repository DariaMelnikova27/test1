import allure
from selenium.webdriver.common.by import By
from page_object.BasePage import BasePage


class GeneralPage(BasePage):
    """ Класс главной страницы"""
    page_url = ""

    AUTH_LOGO = (By.LINK_TEXT, "Личный кабинет")
    SPECTACLE = (By.XPATH, "/html/body/header/div/nav[1]/ul/li[1]/a")


    def check_elements_on_general_page(self):
        """ Метод проверки видимости элементов на главной странице """
        self._find_element(GeneralPage.AUTH_LOGO)
        self._find_element(GeneralPage.SPECTACLE)


    @allure.step("Кликаю по разделу сайта СПЕТАКЛИ")
    def click_spectacle_section(self):
        self.click(self.element(self.SPECTACLE))
        return self


