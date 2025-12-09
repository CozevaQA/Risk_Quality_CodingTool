
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Risk_POC import Risk_POC
from utils import web_utils as webfunctions
from pages.BasePage import BasePage


class Patient_Dashboard(BasePage) :
# Accepts a cozeva id from Test Layer and do operations
    hcc_table='//div[@id="hcc_measures"]'
    non_compliant_dx='//div[@class="poc_dashboard pbb"]//child::div[@prev_status="red_dot"]//following-sibling::div[@class="clear dx_detail"]//child::div[contains(@class,"dx_row current_yr")]'
    first_pencil_icon= '(//div[@class="poc_dashboard pbb"]//child::i)[1]'
    open_poc_button= '(//a[text()="Confirm/Disconfirm"])[1]'
    dx_codes= '//div[@class="code_details col careops-new"]'

    def __init__(self,driver,timeout,cozeva_id):
        super().__init__(driver,timeout)
        self.cozeva_id=cozeva_id

    def open_patient_dashboard(self,baseurl):
        base=baseurl
        endpoint=f"/patient_detail/{self.cozeva_id}?tab_type=CareOps&session=YXBwX2lkPXJlZ2lzdHJpZXMmcGF5ZXJJZD01NTEwJmN1c3RJZD01NTEwJnZncElkPTU1MTAmdnBJZD01NTEwJnZnMElkPTU1MTAmaG9tZT1ZWEJ3WDJsa1BYSmxaMmx6ZEhKcFpYTW1ZM1Z6ZEVsa1BUVTFNVEFtY0dGNVpYSkpaRDAxTlRFd0ptOXlaMGxrUFRVMU1UQW1jRlZwWkQweE9UY3lPRE1tZG1kd1NXUTlOVFV4TUNaMmNFbGtQVFUxTVRBbWRtY3dTV1E5TlRVeE1BJTNEJTNEJm9yZ0lkPTU1MTAmcFVpZD0xOTcyODM%3D&cozeva_id=1H5KW1Z&patient_id=84355753"
        url=base+endpoint
        print("url created")
        try:
            print("In try block")
            self.driver.get(url)
            webfunctions.wait_for_page_load(self.driver, 120)
            WebDriverWait(self.driver, 120).until(
                EC.visibility_of_element_located((By.XPATH, self.hcc_table)))
            return True
        except Exception as e:
            return False


    def get_non_compliant_dx(self):
        # Initialize here
        non_compliant_dx = []
        dx_code_list_elements = self.driver.find_elements(By.XPATH, self.non_compliant_dx)
        for dx_code_list_element in dx_code_list_elements:
            non_compliant_dx.append(dx_code_list_element.get_attribute("id"))
        print(f"List of DX {non_compliant_dx}")
        return non_compliant_dx

    def open_poc(self):
        pencil_icon = self.driver.find_element(By.XPATH, self.first_pencil_icon)
        webfunctions.action_click(self.driver, pencil_icon)

        try:
            print("Looking for Confirm/Disconfirm button...")
            open_poc_button = self.driver.find_element(By.XPATH, self.open_poc_button)
            print("open_poc_button FOUND")

            print("Clicking Confirm/Disconfirm...")
            webfunctions.action_click(self.driver, open_poc_button)
            print("Clicked. Waiting for page load...")

            webfunctions.wait_for_page_load(self.driver, 40)
            print("Page load done.")

            risk_poc=Risk_POC(self.driver,self.timeout)
            return risk_poc

        except Exception as e:
            print("open_poc failed because:", e)
            raise e
            return False



