from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.RiskPOC import Risk_POC
from utils import web_utils as webfunctions
from pages.BasePage import BasePage
from pages.locators.PatientDashboardLocators import PatientDashboardLocators


class Patient_Dashboard(BasePage):

    def __init__(self, driver, timeout, cozeva_id):
        super().__init__(driver, timeout)
        self.cozeva_id = cozeva_id

    def open_patient_dashboard(self, baseurl):
        base = baseurl

        endpoint = (
            f"/patient_detail/{self.cozeva_id}?tab_type=CareOps&session=YXBwX2lkPXJlZ2lzdHJpZXMmcGF5ZXJJZD01NTEwJmN1c3RJZD01NTEwJnZncElkPTU1MTAmdnBJZD01NTEwJnZnMElkPTU1MTAmaG9tZT1ZWEJ3WDJsa1BYSmxaMmx6ZEhKcFpYTW1ZM1Z6ZEVsa1BUVTFNVEFtY0dGNVpYSkpaRDAxTlRFd0ptOXlaMGxrUFRVMU1UQW1jRlZwWkQweE9UY3lPRE1tZG1kd1NXUTlOVFV4TUNaMmNFbGtQVFUxTVRBbWRtY3dTV1E5TlRVeE1BJTNEJTNEJm9yZ0lkPTU1MTAmcFVpZD0xOTcyODM%3D&cozeva_id=1H5KW1Z&patient_id=84355753"
        )

        url = base + endpoint
        print("url created:", url)

        try:
            print("In try block")
            self.driver.get(url)

            webfunctions.wait_for_page_load(self.driver, 120)

            WebDriverWait(self.driver, 120).until(
                EC.visibility_of_element_located(PatientDashboardLocators.HCC_TABLE)
            )

            return True

        except Exception as e:
            print("Failed to load patient dashboard:", e)
            return False

    def get_non_compliant_dx(self):
        non_compliant_dx = []

        dx_code_elements = self.driver.find_elements(
            *PatientDashboardLocators.NON_COMPLIANT_DX
        )

        for element in dx_code_elements:
            non_compliant_dx.append(element.get_attribute("id"))

        print(f"List of DX {non_compliant_dx}")
        return non_compliant_dx

    def open_poc(self):
        # Click pencil icon
        pencil_icon = self.driver.find_element(
            *PatientDashboardLocators.FIRST_PENCIL_ICON
        )
        webfunctions.action_click(self.driver, pencil_icon)

        try:
            print("Looking for Confirm/Disconfirm button...")

            open_poc_button = self.driver.find_element(
                *PatientDashboardLocators.OPEN_POC_BUTTON
            )
            print("open_poc_button FOUND")

            print("Clicking Confirm/Disconfirm...")
            webfunctions.action_click(self.driver, open_poc_button)
            print("Clicked. Waiting for page load...")

            webfunctions.wait_for_page_load(self.driver, 40)
            print("Page load done.")

            return Risk_POC(self.driver, self.timeout)

        except Exception as e:
            print("open_poc failed because:", e)
            raise e