import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from data.urls import BASE_URL
from pages.register_page import RegisterPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    # Чистый профиль — без расширений и балунов
    options.add_argument("--disable-extensions")       # отключает расширения
    options.add_argument("--disable-notifications")    # отключает всплывающие уведомления

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
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
    email = f"test_{int(time.time() * 1000)}@ya.ru"
    password = "password123"
    name = "Тестовый Пользователь"

    driver.get(base_url + "register")
    RegisterPage(driver).register(name, email, password)

    yield {
        "email": email,
        "password": password,
        "name": name,
    }
