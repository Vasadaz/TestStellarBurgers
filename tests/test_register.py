import time

from data.test_data import generate_email
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


class TestRegistration:

    def test_successful_registration(self, driver, base_url):
        driver.get(base_url + "register")

        # Регистрация уникального пользователя
        RegisterPage(driver).register("Тестовый Пользователь", generate_email(), "password123")

        assert LoginPage(driver).is_login_button_displayed(), (
            "После успешной регистрации не отобразилась страница входа"
        )

    def test_registration_with_short_password_shows_error(self, driver, base_url):
        driver.get(base_url + "register")

        email = f"test_{int(time.time() * 1000)}@ya.ru"
        register_page = RegisterPage(driver)
        register_page.register("Тестовый Пользователь", email, "12345")

        assert register_page.is_error_displayed(), "Ошибка валидации пароля не отобразилась"
