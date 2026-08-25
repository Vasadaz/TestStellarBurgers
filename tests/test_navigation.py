from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from data.urls import LOGIN_PAGE

class TestNavigation:
    def test_navigate_to_constructor_via_button(self, driver, registered_user):
        """Переход из ЛК в конструктор по кнопке «Конструктор»."""
        LoginPage(driver).open_and_login(registered_user["email"], registered_user["password"])
        Header(driver).click_profile_button()
        ProfilePage(driver).wait_until_loaded()

        Header(driver).click_constructor_button()

        # Маркер главной страницы — кнопка «Войти в аккаунт» или заголовок конструктора
        assert MainPage(driver).is_constructor_loaded(), "Конструктор не открылся по кнопке"

    def test_navigate_to_constructor_via_logo(self, driver, registered_user):
        """Переход из ЛК в конструктор по клику на логотип Stellar Burgers."""
        LoginPage(driver).open_and_login(registered_user["email"], registered_user["password"])
        Header(driver).click_profile_button()
        ProfilePage(driver).wait_until_loaded()

        Header(driver).click_logo()

        assert MainPage(driver).is_constructor_loaded(), "Конструктор не открылся по логотипу"
