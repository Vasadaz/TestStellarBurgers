# tests/test_login.py
import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.header import Header
from pages.profile_page import ProfilePage

class TestLogin:

    def _open_login_via_main_button(self, driver, base_url):
        driver.get(base_url)
        MainPage(driver).click_login_button()

    def _open_login_via_profile_button(self, driver, base_url):
        driver.get(base_url)
        Header(driver).click_profile_button()

    def _open_login_via_registration_link(self, driver, base_url):
        driver.get(base_url + "register")
        RegisterPage(driver).click_login_link()

    def _open_login_via_forgot_password_link(self, driver, base_url):
        driver.get(base_url + "forgot-password")
        ForgotPasswordPage(driver).click_login_link()

    @pytest.mark.parametrize("open_login", [
        _open_login_via_main_button,
        _open_login_via_profile_button,
        _open_login_via_registration_link,
        _open_login_via_forgot_password_link,
    ])
    def test_login_from_different_entry_points(self, driver, base_url, registered_user, open_login):
        open_login(self, driver, base_url)

        login_page = LoginPage(driver)
        assert login_page.is_login_button_displayed(), "Форма входа не отобразилась"

        login_page.login(registered_user["email"], registered_user["password"])

        # После входа сервис может вернуть на главную — переходим в ЛК явно
        Header(driver).click_profile_button()

        profile = ProfilePage(driver)
        profile.wait_until_loaded()

        assert profile.is_logout_displayed(), "Вход не выполнен: нет кнопки «Выйти»"
