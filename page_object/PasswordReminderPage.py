import allure
from selenium.webdriver.common.by import By
from page_object.BasePage import BasePage


class PasswordReminderPage(BasePage):
    """ Класс страницы восстановления пароля """
    page_url = "login/reminder"

    EMAIL_INPUT = (By.NAME, "contact")
    REMINDER_BUTTON = (By.CSS_SELECTOR, ".registration-button")
    REG_EMAIL_ERROR = (By.CSS_SELECTOR, ".reg-email-error")

    def check_elements_on_reminder_page(self):
        """ Метод проверки видимости элементов на странице восстановления пароля """
        self._find_element(PasswordReminderPage.EMAIL_INPUT)
        self._find_element(PasswordReminderPage.REMINDER_BUTTON)
        self._find_element(PasswordReminderPage.REG_EMAIL_ERROR)

    @allure.step("Заполняю поле email значением {email}")
    def email_fill(self, email):
        self._input(self.element(self.EMAIL_INPUT), email)
        return self

    @allure.step("Нажимаю кнопку Восстановить")
    def reminder_button_click(self):
        self.click(self.element(self.REMINDER_BUTTON))
        return self

    @property
    @allure.step("Проверяю наличие ошибки некорректно введенного email")
    def unsuccess_email_msg(self):
        msg = self.element(self.REG_EMAIL_ERROR)
        return msg.text
