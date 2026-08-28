from selenium.webdriver.common.by import By

class ProfilePageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Логин')]/following-sibling::input")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
