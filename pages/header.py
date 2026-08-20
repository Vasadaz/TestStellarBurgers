# pages/header.py
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class Header(BasePage):
    def click_profile_button(self):
        """Клик по кнопке «Личный кабинет» в шапке."""
        self.click(HeaderLocators.PROFILE_BUTTON)

    def click_constructor_button(self):
        """Клик по кнопке «Конструктор»."""
        self.click(HeaderLocators.CONSTRUCTOR_BUTTON)

    def click_logo(self):
        """Клик по логотипу Stellar Burgers."""
        self.click(HeaderLocators.LOGO)
