# tests/test_navigation.py
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from data.urls import BASE_URL

class TestNavigation:

    def _login_and_open_profile(self, driver, base_url, registered_user):
        """Авторизуется и переходит в личный кабинет."""
        driver.get(base_url + "login")
        LoginPage(driver).login(registered_user["email"], registered_user["password"])
        Header(driver).click_profile_button()
        ProfilePage(driver).wait_until_loaded()

    def test_navigate_to_constructor_via_button(self, driver, base_url, registered_user):
        """Переход из ЛК в конструктор по кнопке «Конструктор»."""
        self._login_and_open_profile(driver, base_url, registered_user)

        Header(driver).click_constructor_button()

        # Маркер главной страницы — кнопка «Войти в аккаунт» или заголовок конструктора
        assert MainPage(driver).is_constructor_loaded(), "Конструктор не открылся по кнопке"

    def test_navigate_to_constructor_via_logo(self, driver, base_url, registered_user):
        """Переход из ЛК в конструктор по клику на логотип Stellar Burgers."""
        self._login_and_open_profile(driver, base_url, registered_user)

        Header(driver).click_logo()

        assert MainPage(driver).is_constructor_loaded(), "Конструктор не открылся по логотипу"
