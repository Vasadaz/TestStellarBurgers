from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    def click_login_link(self):
        """Клик по ссылке «Войти» в форме восстановления пароля."""
        self.click(ForgotPasswordPageLocators.LOGIN_LINK)
