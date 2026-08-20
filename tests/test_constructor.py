import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test__constructor__transfer_to_buns__true():
    root_host = 'https://stellarburgers.education-services.ru/'

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    clickable = expected_conditions.element_to_be_clickable

    driver.get(root_host)

    # Переход в раздел 'Начинки'
    wait.until(clickable((By.XPATH, ".//span[text()='Начинки']")))
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()

    # Переход в раздел 'Булки'
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()

    # Проверяем результат перехода
    element_class = driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::div").get_attribute('class')
    assert 'tab_tab_type_current' in element_class

    driver.quit()


def test__constructor__transfer_to_sauces__true():
    root_host = 'https://stellarburgers.education-services.ru/'

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    clickable = expected_conditions.element_to_be_clickable

    driver.get(root_host)

    # Переход в раздел 'Соусы'
    wait.until(clickable((By.XPATH, ".//span[text()='Соусы']")))
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()

    # Проверяем результат перехода
    element_class = driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::div").get_attribute('class')
    assert 'tab_tab_type_current' in element_class

    driver.quit()


def test__constructor__transfer_to_toppings__true():
    root_host = 'https://stellarburgers.education-services.ru/'

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    clickable = expected_conditions.element_to_be_clickable

    driver.get(root_host)

    # Переход в раздел 'Начинки'
    wait.until(clickable((By.XPATH, ".//span[text()='Начинки']")))
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()

    # Проверяем результат перехода
    element_class = driver.find_element(By.XPATH, ".//span[text()='Начинки']/parent::div").get_attribute('class')
    assert 'tab_tab_type_current' in element_class

    driver.quit()


if __name__ == "__main__":
    test__constructor__transfer_to_personal_account__true()
    test__constructor__transfer_to_sauces__true()
    test__constructor__transfer_to_toppings__true()