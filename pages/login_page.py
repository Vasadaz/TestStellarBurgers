from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.header import Header
from pages.register_page import RegisterPage
from pages.forgot_password_page import ForgotPasswordPage
from locators.login_locators import LoginPageLocators
from data.urls import BASE_URL, REGISTER_PAGE, FORGOT_PASSWORD_PAGE, LOGIN_PAGE


class LoginPage(BasePage):
    def input_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        """Заполняет форму и отправляет её (счастливый путь)."""
        self.input_email(email)
        self.input_password(password)
        self.click_login()

    def is_login_button_displayed(self):
        return self.is_displayed(LoginPageLocators.LOGIN_BUTTON)

    def wait_for_current_url(self, expected_url):
        """Ждёт, пока URL станет ожидаемым (после успешного входа)."""
        return self.wait.until(lambda d: d.current_url == expected_url)

    def click_recover_link(self):
        """Клик по ссылке «Восстановить пароль»."""
        self.click(LoginPageLocators.RECOVER_LINK)

    def open_login_via_main_button(self):
        """Переход к форме входа через кнопку «Войти в аккаунт» на главной."""
        self.open(BASE_URL)
        MainPage(self.driver).click_login_button()

    def open_login_via_profile_button(self):
        """Переход к форме входа через кнопку «Личный кабинет» в шапке."""
        self.open(BASE_URL)
        Header(self.driver).click_profile_button()

    def open_login_via_registration_link(self):
        """Переход к форме входа через ссылку «Войти» на странице регистрации."""
        self.open(REGISTER_PAGE)
        RegisterPage(self.driver).click_login_link()

    def open_login_via_forgot_password_link(self):
        """Переход к форме входа через ссылку «Войти» на странице восстановления пароля."""
        self.open(FORGOT_PASSWORD_PAGE)
        ForgotPasswordPage(self.driver).click_login_link()

    def open_and_login(self, email, password):
        """Открывает страницу входа и авторизуется."""
        self.open(LOGIN_PAGE)
        self.login(email, password)
