import allure
from selenium.webdriver.common.by import By
from page_object.BasePage import BasePage


class LoginPage(BasePage):
    """ Класс страницы авторизации """
    page_url = "login"

    LOGIN_INPUT = (By.NAME, "LoginForm[contact]")
    PASSWORD_INPUT = (By.NAME, "LoginForm[password]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".registration-button")
    ERROR_MSG = (By.CSS_SELECTOR, ".login-msg")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchForm .old-input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".find_button .btn3")
    SEARCH_ERROR_MSG = (By.XPATH, "/html/body/main/div[5]/div/div/div/div/div/div[1]/section[4]/p")

    def check_elements_on_login_page(self):
        """ Метод проверки видимости элементов на странице авторизации """
        self._find_element(LoginPage.LOGIN_INPUT)
        self._find_element(LoginPage.PASSWORD_INPUT)
        self._find_element(LoginPage.SUBMIT_BUTTON)
        self._find_element(LoginPage.ERROR_MSG)
        self._find_element(LoginPage.SEARCH_INPUT)
        self._find_element(LoginPage.SEARCH_BUTTON)
        self._find_element(LoginPage.SEARCH_ERROR_MSG)

    @allure.step("Заполняю поле логина значением {login}")
    def login_fill(self, login):
        self._input(self.element(self.LOGIN_INPUT), login)
        return self

    @allure.step("Заполняю поле пароля значением {password}")
    def password_fill(self, password):
        self._input(self.element(self.PASSWORD_INPUT), password)
        return self

    @allure.step("Нажимаю кнопку Войти")
    def submit_button_click(self):
        self.click(self.element(self.SUBMIT_BUTTON))
        return self

    @property
    @allure.step("Проверяю наличие ошибки авторизации")
    def unsuccess_login_msg(self):
        msg = self.element(self.ERROR_MSG)
        return msg.text

    @allure.step("Заполняю поле поиска значением {search_input}")
    def search_fill(self, search_input):
        self._input(self.element(self.SEARCH_INPUT), search_input)
        return self

    @allure.step("Нажимаю кнопку ПОИСК")
    def search_button_click(self):
        self.click(self.element(self.SEARCH_BUTTON))
        return self

    @property
    @allure.step("Проверяю наличие cообщения о ненайденных мероприятиях")
    def unsuccess_search_msg(self):
        msg = self.element(self.SEARCH_ERROR_MSG)
        return msg.text
