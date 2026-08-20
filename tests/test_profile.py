from pages.header import Header
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data.urls import LOGIN_PAGE, PROFILE_PAGE

class TestProfile:

    def _login(self, driver, base_url, registered_user):
        """Вспомогательный шаг авторизации перед проверками ЛК."""
        driver.get(base_url + "login")
        LoginPage(driver).login(registered_user["email"], registered_user["password"])

    def test_transition_to_profile(self, driver, base_url, registered_user):
        """Переход в личный кабинет по клику на «Личный кабинет» (до авторизации — редирект на вход)."""
        self._login(driver, base_url, registered_user)

        # После входа переходим в ЛК по кнопке в шапке
        Header(driver).click_profile_button()

        profile = ProfilePage(driver)
        profile.wait_until_loaded()

        assert profile.is_logout_displayed(), "Личный кабинет не открылся: нет кнопки «Выйти»"
        assert "account" in driver.current_url, "URL не соответствует личному кабинету"

    def test_logout_from_profile(self, driver, base_url, registered_user):
        """Выход из аккаунта по кнопке «Выйти»."""
        self._login(driver, base_url, registered_user)

        Header(driver).click_profile_button()
        profile = ProfilePage(driver)
        profile.wait_until_loaded()

        profile.click_logout()

        # После выхода попадаем на форму входа
        assert LoginPage(driver).is_login_button_displayed(), (
            "После выхода не отобразилась форма входа"
        )
