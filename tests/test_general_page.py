import allure
import requests
from allure_commons.types import Severity
from page_object.GeneralPage import GeneralPage

""" Тесты главной страницы """

page_url = "https://spb.ticketland.ru/"


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на главной странице')
@allure.title('Проверка видимости элементов на главной странице')
def test_elements_general_page(browser):
    page = GeneralPage(browser)
    page.open_page(browser)
    page.check_elements_on_general_page()


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на главной странице')
@allure.title('Проверка корректного кода ответа (200)')
def test_get_status_code_equals_200():
    response = requests.get(page_url)
    assert response.status_code == 200


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на главной странице')
@allure.title('Проверка возможности перехода в раздел СПЕКТАКЛИ')
def test_open_spectacle_section(browser):
    page = GeneralPage(browser)
    page.open_page(browser)
    page.click_spectacle_section
