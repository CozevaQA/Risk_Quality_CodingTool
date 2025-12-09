
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, by_locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def wait_for_clickable(self, by_locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(by_locator)
        )