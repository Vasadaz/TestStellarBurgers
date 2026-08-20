import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test__registration__not_valid_password__false():
    root_host = 'https://stellarburgers.education-services.ru'
    user_name = 'Николай'
    user_email = f"sysoev_53_{random.randint(000000, 999999)}@gmail.com"
    user_password = "12345"

    driver = webdriver.Chrome()
    driver.get(root_host)

    # Переход к форме регистрации
    driver.find_element(By.XPATH, ".//nav/a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() # Ссылка "Зарегистрироваться"

    # Выполняем регистрацию
    driver.find_elements(By.NAME, "name")[0].send_keys(user_name) # Вводим имя
    driver.find_elements(By.NAME, "name")[1].send_keys(user_email) # Вводим email
    driver.find_element(By.NAME, "Пароль").send_keys(user_password) # Вводим пароль
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"

    # Проверка на появление предупреждения о корректность пароля
    err_red_border_elm = driver.find_element(By.CLASS_NAME, 'input_status_error')
    err_red_text_elm = driver.find_element(By.CLASS_NAME, 'input__error')

    assert err_red_border_elm and err_red_text_elm.text == 'Некорректный пароль'

    driver.quit()


def test__registration__valid_all_data__true():
    root_host = 'https://stellarburgers.education-services.ru'
    user_name = 'Николай'
    user_email = f"sysoev_53_{random.randint(000000, 999999)}@gmail.com"
    user_password = "123456"

    driver = webdriver.Chrome()
    driver.get(root_host)

    # Переход к форме регистрации
    driver.find_element(By.XPATH, ".//nav/a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click() # Ссылка "Зарегистрироваться"

    # Выполняем регистрацию
    driver.find_elements(By.NAME, "name")[0].send_keys(user_name) # Вводим имя
    driver.find_elements(By.NAME, "name")[1].send_keys(user_email) # Вводим email
    driver.find_element(By.NAME, "Пароль").send_keys(user_password) # Вводим пароль
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click() # Кнопка "Зарегистрироваться"

    # Входим в аккаунт
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
    driver.find_element(By.NAME, "name").send_keys(user_email)
    driver.find_element(By.NAME, "Пароль").send_keys(user_password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click() # Кнопка "Войти"

    # Проверяем результат регистрации
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//nav/a[@href='/account']")))
    driver.find_element(By.XPATH, ".//nav/a[@href='/account']").click() # Кнопка(как ссылка) "Личный кабинет"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.NAME, "Name")))
    assert driver.find_element(By.NAME, "Name").get_attribute("value") == user_name # Проверка имени пользователя

    driver.quit()


if __name__ == "__main__":
    test__registration__not_valid_password__false()
    test__registration__valid_all_data__true()
