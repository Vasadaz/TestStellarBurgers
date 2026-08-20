from selenium.webdriver.common.by import By

class HeaderLocators:
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

    # Кнопка «Конструктор» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href,'/')]/p[contains(text(),'Конструктор')]")

    # Кнопка «Личный кабинет» в шапке
    PROFILE_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]/p[contains(text(),'Личный Кабинет')]")
