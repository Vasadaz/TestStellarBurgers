import time

VALID_NAME = "Тестовый Пользователь"
VALID_PASSWORD = "password123"
SHORT_PASSWORD = "12345"          # меньше 6 символов
EXPECTED_PASSWORD_ERROR = "Некорректный пароль"

def generate_email():
    return f"test_{int(time.time() * 1000)}@ya.ru"
