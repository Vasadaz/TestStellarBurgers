from pages.main_page import MainPage
from locators.main_locators import MainPageLocators
from data.urls import BASE_URL


class TestConstructor:
    def test_section_navigation_to_buns(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        tab_locator = MainPageLocators.BUNS_SECTION

        # Раздел «Булки» активирован по умолчанию, поэтому сначала переходим в раздел «Соусы».
        main_page.click_tab(MainPageLocators.SAUCES_SECTION)

        # Переходы к разделу «Булки»
        main_page.click_tab(tab_locator)

        # Раздел считается активным, если у его таба появился класс current
        assert main_page.is_tab_active(tab_locator), f"Раздел не активировался: {tab_locator}"

    def test_section_navigation_to_sauces(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        tab_locator = MainPageLocators.SAUCES_SECTION

        # Переход в раздел "Соусы"
        main_page.click_tab(tab_locator)

        # Раздел считается активным, если у его таба появился класс current
        assert main_page.is_tab_active(tab_locator), f"Раздел не активировался: {tab_locator}"

    def test_section_navigation_to_fillings(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)
        tab_locator = MainPageLocators.FILLINGS_SECTION

        # Переход в раздел "Начинки"
        main_page.click_tab(tab_locator)

        # Раздел считается активным, если у его таба появился класс current
        assert main_page.is_tab_active(tab_locator), f"Раздел не активировался: {tab_locator}"
