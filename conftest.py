import pytest
from selenium import webdriver

from data.test_data import generate_email
from data.urls import REGISTER_PAGE
from pages.register_page import RegisterPage


@pytest.fixture(scope="function")
def driver():
    # Ручной запуск через путь к драйверу
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    yield browser
    browser.quit()

@pytest.fixture
def registered_user(driver):
    """
    Регистрирует нового пользователя через UI.
    Возвращает словарь с уникальными email/password/name.
    """
    email = generate_email()
    password = "password123"
    name = "Тестовый Пользователь"

    driver.get(REGISTER_PAGE)
    RegisterPage(driver).register(name, email, password)

    return {
        "email": email,
        "password": password,
        "name": name,
    }
