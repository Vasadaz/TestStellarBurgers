from pages.header import Header
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data.urls import LOGIN_PAGE

class TestProfile:
    def test_transition_to_profile(self, driver, registered_user):
        """Переход в личный кабинет по клику на «Личный кабинет»."""
        # Авторизация через Page Object
        LoginPage(driver).open_and_login(registered_user["email"], registered_user["password"])

        # Переход в ЛК по кнопке в шапке
        Header(driver).click_profile_button()

        profile = ProfilePage(driver)
        profile.wait_until_loaded()

        assert profile.is_on_profile_page(), "URL не соответствует личному кабинету"

    def test_logout_from_profile(self, driver, registered_user):
        """Выход из аккаунта по кнопке «Выйти»."""
        # Авторизация через Page Object
        LoginPage(driver).open_and_login(registered_user["email"], registered_user["password"])

        Header(driver).click_profile_button()
        profile = ProfilePage(driver)
        profile.wait_until_loaded()

        profile.click_logout()

        # После выхода попадаем на форму входа
        assert LoginPage(driver).is_login_button_displayed(), "После выхода не отобразилась форма входа"
