from pages.base_page import BasePage
from locators.profile_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def click_logout(self):
        """Клик по кнопке «Выйти» в личном кабинете."""
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def get_profile_email(self):
        """Возвращает email в поле «Логин» личного кабинета."""
        return self.get_attribute(ProfilePageLocators.EMAIL_INPUT, "value")

    def get_profile_name(self):
        """Возвращает имя в поле «Имя» личного кабинета."""
        return self.get_attribute(ProfilePageLocators.NAME_INPUT, "value")

    def is_logout_displayed(self):
        """Проверяет отображение кнопки «Выйти» (признак авторизации)."""
        return self.is_displayed(ProfilePageLocators.LOGOUT_BUTTON)

    def wait_until_loaded(self):
        """Ждёт появления кнопки «Выйти» — маркер загруженного профиля."""
        self.wait.until(
            lambda d: self.is_displayed(ProfilePageLocators.LOGOUT_BUTTON)
        )
        return self
