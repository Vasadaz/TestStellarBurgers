import pytest

from pages.login_page import LoginPage
from pages.header import Header
from pages.profile_page import ProfilePage

class TestLogin:

    @pytest.mark.parametrize("open_login", [
        LoginPage.open_login_via_main_button,
        LoginPage.open_login_via_profile_button,
        LoginPage.open_login_via_registration_link,
        LoginPage.open_login_via_forgot_password_link,
    ])
    def test_login_from_different_entry_points(self, driver, registered_user, open_login):
        # Переход к варианту входа
        open_login(driver)

        login_page = LoginPage(driver)
        login_page.login(registered_user["email"], registered_user["password"])

        # Переход в ЛК
        Header(driver).click_profile_button()

        profile = ProfilePage(driver)
        profile.wait_until_loaded()

        assert profile.is_logout_displayed(), "Вход не выполнен: нет кнопки «Выйти»"
