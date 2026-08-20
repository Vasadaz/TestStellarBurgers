from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators

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
        return self.wait.until(
            lambda d: d.current_url == expected_url
        )

    def click_recover_link(self):
        """Клик по ссылке «Восстановить пароль»."""
        self.click(LoginPageLocators.RECOVER_LINK)
