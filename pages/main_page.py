from pages.base_page import BasePage
from locators.main_locators import MainPageLocators

class MainPage(BasePage):
    def click_login_button(self):
        """Клик по кнопке «Войти в аккаунт» на главной."""
        self.click(MainPageLocators.LOGIN_BUTTON)

    def is_constructor_loaded(self):
        """Проверяет загрузку конструктора — по заголовку «Соберите бургер»."""
        return self.is_displayed(MainPageLocators.CONSTRUCTOR_HEADER)

    def click_tab(self, tab_locator):
        """Клик по табу раздела ингредиентов."""
        self.click(tab_locator)

    def is_tab_active(self, tab_locator):
        """Проверяет, что таб стал активным (класс current)."""
        element = self.find(tab_locator)
        return "current" in element.get_attribute("class")

