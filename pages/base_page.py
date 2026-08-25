from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False

    def current_url(self):
        return self.driver.current_url

    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)
