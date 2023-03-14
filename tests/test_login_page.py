import allure
import pytest
from allure_commons.types import Severity
from page_object.LoginPage import LoginPage

""" Тесты страницы авторизации """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на странице авторизации')
@allure.title('Проверка видимости элементов на странице авторизации')
def test_elements_login_page(browser):
    page = LoginPage(browser)
    page.open_page(browser)
    page.check_elements_on_login_page()


@allure.severity(severity_level=Severity.BLOCKER)
@allure.feature('Действия на странице авторизации')
@allure.title('Авторизация с корректными данными')
def test_successful_login(browser):
    page = LoginPage(browser)
    page.open_page(browser)
    page.login_fill("dariatest11@yandex.ru")
    page.password_fill("Qwe12345++")
    page.submit_button_click()


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на странице авторизации')
@allure.title('Авторизация с некорректными данными')
@pytest.mark.parametrize('login', [' ', '123', 'Aaa', 'aaa@ya.ru', '@ya.ru'])
@pytest.mark.parametrize('password', [' ', '123', 'Qwe', '!@$', 'Qwe123!'])
def test_unsuccessful_login(browser, login, password):
    page = LoginPage(browser)
    page.open_page(browser)
    page.login_fill(login)
    page.password_fill(password)
    page.submit_button_click()
    assert "" in page.unsuccess_login_msg


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на странице авторизации')
@allure.title('Результативный поиск')
def test_successful_search(browser):
    page = LoginPage(browser)
    page.open_page(browser)
    page.search_fill("Юнона и Авось")
    page.search_button_click()


@allure.severity(severity_level=Severity.MINOR)
@allure.feature('Действия на странице авторизации')
@allure.title('Нерезультативный поиск (ничего не найдено)')
@pytest.mark.parametrize('search_data', ['Aaa', 'a123', '___!"@', 'ЫЪь', 'Длинный поисковый запрос ввежу в поисковую строку'])
def test_unsuccessful_search(browser, search_data):
    page = LoginPage(browser)
    page.open_page(browser)
    page.search_fill(search_data)
    page.search_button_click()
    assert "" in page.unsuccess_search_msg
