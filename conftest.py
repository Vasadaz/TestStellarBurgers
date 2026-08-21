import time

import pytest
from selenium import webdriver

from data.test_data import generate_email
from data.urls import BASE_URL
from pages.register_page import RegisterPage


@pytest.fixture(scope="function")
def driver():
    # Ручной запуск через путь к драйверу
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    yield browser
    browser.quit()

@pytest.fixture
def base_url():
    """Базовый URL сервиса."""
    return BASE_URL

@pytest.fixture
def registered_user(driver, base_url):
    """
    Регистрирует нового пользователя через UI.
    Возвращает словарь с уникальными email/password/name.
    """
    email = generate_email()
    password = "password123"
    name = "Тестовый Пользователь"

    driver.get(base_url + "register")
    RegisterPage(driver).register(name, email, password)

    yield {
        "email": email,
        "password": password,
        "name": name,
    }
