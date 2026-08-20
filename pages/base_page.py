from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        # Клик через JS — обходит перекрывающие элементы (балуны, тултипы)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url

    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)
