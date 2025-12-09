from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import web_utils as webfunctions
from pages.BasePage import BasePage

class Risk_POC(BasePage):
    POC_DX = (By.XPATH, '//div[@class="dx_code_div gray_background"]//child::div')
    SHOW_DX_BUTTON = (By.XPATH, '//div[@class="collapse flex"]')

    def is_page_loaded(self):
        # use explicit waits to be more robust
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.POC_DX)
        )
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.SHOW_DX_BUTTON)
        )
        return self
    #def _get_all_noncompliant_dx_codes(self):


