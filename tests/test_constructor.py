import pytest

from pages.main_page import MainPage
from locators.main_locators import MainPageLocators

class TestConstructor:

    @pytest.mark.parametrize("tab_locator", [
        MainPageLocators.BUNS_SECTION,
        MainPageLocators.SAUCES_SECTION,
        MainPageLocators.FILLINGS_SECTION,
    ])
    def test_section_navigation(self, driver, base_url, tab_locator):
        """Переходы к разделам «Булки», «Соусы», «Начинки»."""
        driver.get(base_url)

        main_page = MainPage(driver)
        main_page.click_tab(tab_locator)

        # Раздел считается активным, если у его таба появился класс current
        assert main_page.is_tab_active(tab_locator), (
            f"Раздел не активировался: {tab_locator}"
        )
