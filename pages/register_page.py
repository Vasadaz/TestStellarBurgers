from pages.base_page import BasePage
from locators.register_locators import RegisterPageLocators

class RegisterPage(BasePage):
    def fill_name(self, name):
        self.input_text(RegisterPageLocators.NAME_INPUT, name)

    def fill_email(self, email):
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.input_text(RegisterPageLocators.PASSWORD_INPUT, password)

    def click_register(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    def register(self, name, email, password):
        """Заполняет форму и отправляет её (счастливый путь)."""
        self.fill_name(name)
        self.fill_email(email)
        self.fill_password(password)
        self.click_register()

    def get_error_text(self):
        """Возвращает текст ошибки валидации пароля."""
        return self.get_text(RegisterPageLocators.PASSWORD_ERROR)

    def is_error_displayed(self):
        """Проверяет, что ошибка пароля отображается на странице."""
        return self.is_displayed(RegisterPageLocators.PASSWORD_ERROR)

    def wait_for_login_page(self):
        self.wait.until(lambda d: "login" in d.current_url)
        return self.is_displayed(RegisterPageLocators.LOGIN_LINK)

    def click_login_link(self):
        """Клик по ссылке «Войти» в форме регистрации."""
        self.click(RegisterPageLocators.LOGIN_LINK)
