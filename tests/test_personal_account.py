import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test__personal_account__transfer_to_personal_account__true():
    root_host = 'https://stellarburgers.education-services.ru/'
    user_name = 'Николай'
    user_email = f"sysoev_53_{random.randint(000000, 999999)}@gmail.com"
    user_password = "123456"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    clickable = expected_conditions.element_to_be_clickable

    driver.get(root_host)

    # Переход к форме регистрации
    driver.find_element(By.XPATH, ".//a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() # Ссылка "Зарегистрироваться"

    # Выполняем регистрацию
    driver.find_elements(By.NAME, "name")[0].send_keys(user_name) # Вводим имя
    driver.find_elements(By.NAME, "name")[1].send_keys(user_email) # Вводим email
    driver.find_element(By.NAME, "Пароль").send_keys(user_password) # Вводим пароль
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"

    # Входим в аккаунт
    wait.until(clickable((By.XPATH, ".//button[text()='Войти']")))
    driver.find_element(By.NAME, "name").send_keys(user_email)
    driver.find_element(By.NAME, "Пароль").send_keys(user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"

    # Проверяем результат входа
    wait.until(clickable((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    wait.until(expected_conditions.visibility_of_element_located((By.NAME, "Name")))

    assert '/account' in driver.current_url

    driver.quit()


def test__personal_account__transfer_to_constructor__true():
    root_host = 'https://stellarburgers.education-services.ru/'
    user_name = 'Николай'
    user_email = f"sysoev_53_{random.randint(000000, 999999)}@gmail.com"
    user_password = "123456"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    clickable = expected_conditions.element_to_be_clickable

    driver.get(root_host)

    # Переход к форме регистрации
    driver.find_element(By.XPATH, ".//a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() # Ссылка "Зарегистрироваться"

    # Выполняем регистрацию
    driver.find_elements(By.NAME, "name")[0].send_keys(user_name) # Вводим имя
    driver.find_elements(By.NAME, "name")[1].send_keys(user_email) # Вводим email
    driver.find_element(By.NAME, "Пароль").send_keys(user_password) # Вводим пароль
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"

    # Входим в аккаунт
    wait.until(clickable((By.XPATH, ".//button[text()='Войти']")))
    driver.find_element(By.NAME, "name").send_keys(user_email)
    driver.find_element(By.NAME, "Пароль").send_keys(user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"

    # Переходим в личный кабинет
    wait.until(clickable((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"

    # Переходим в конструктор
    wait.until(clickable((By.XPATH, ".//a[@href='/']")))
    driver.find_element(By.XPATH, ".//a[@href='/']").click() # Кнопка(как ссылка) "Конструктор"

    # Проверяем результат входа
    wait.until(clickable((By.XPATH, ".//a[@href='/account']")))
    assert driver.current_url == root_host

    driver.quit()


def test__personal_account__logout__true():
    root_host = 'https://stellarburgers.education-services.ru/'
    user_name = 'Николай'
    user_email = f"sysoev_53_{random.randint(000000, 999999)}@gmail.com"
    user_password = "123456"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    clickable = expected_conditions.element_to_be_clickable

    driver.get(root_host)

    # Переход к форме регистрации
    driver.find_element(By.XPATH, ".//a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() # Ссылка "Зарегистрироваться"

    # Выполняем регистрацию
    driver.find_elements(By.NAME, "name")[0].send_keys(user_name) # Вводим имя
    driver.find_elements(By.NAME, "name")[1].send_keys(user_email) # Вводим email
    driver.find_element(By.NAME, "Пароль").send_keys(user_password) # Вводим пароль
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"

    # Входим в аккаунт
    wait.until(clickable((By.XPATH, ".//button[text()='Войти']")))
    driver.find_element(By.NAME, "name").send_keys(user_email)
    driver.find_element(By.NAME, "Пароль").send_keys(user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"

    # Переходим в личный кабинет
    wait.until(clickable((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"

    # Выходим из личного кабинета
    wait.until(clickable((By.XPATH, ".//button[text()='Выход']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click() # Кнопка "Выход"

    # Проверяем результат входа
    wait.until(clickable((By.XPATH, ".//button[text()='Войти']")))
    assert '/login' in driver.current_url

    driver.quit()


if __name__ == "__main__":
    test__personal_account__transfer_to_personal_account__true()
    test__personal_account__transfer_to_constructor__true()
    test__personal_account__logout__true()
