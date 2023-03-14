import allure
import pytest
from allure_commons.types import Severity
from page_object.PasswordReminderPage import PasswordReminderPage

""" Тесты страницы восстановления пароля """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на странице восстановления пароля')
@allure.title('Проверка видимости элементов на странице восстановления пароля')
def test_elements_password_reminder_page(browser):
    page = PasswordReminderPage(browser)
    page.open_page(browser)
    page.check_elements_on_reminder_page()


@allure.severity(severity_level=Severity.BLOCKER)
@allure.feature('Действия на странице восстановления пароля')
@allure.title('Восстановление пароля с корректными данными')
def test_successful_reminder(browser):
    page = PasswordReminderPage(browser)
    page.open_page(browser)
    page.email_fill("dariatest11@yandex.ru")
    page.reminder_button_click()


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на странице восстановления пароля')
@allure.title('Восстановление пароля с некорректными данными')
@pytest.mark.parametrize('email', [' ', '1', 'Aaa', '!#?', 'a1', 'a1@', 'a1@gmail', '@mail.ru'])
def test_unsuccessful_reminder(browser, email):
    page = PasswordReminderPage(browser)
    page.open_page(browser)
    page.email_fill(email)
    page.reminder_button_click()
    assert "" in page.unsuccess_email_msg
