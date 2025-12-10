# pages/locators/patient_dashboard_locators.py
from selenium.webdriver.common.by import By

class PatientDashboardLocators:
    HCC_TABLE = (By.XPATH, '//div[@id="hcc_measures"]')
    NON_COMPLIANT_DX = (By.XPATH, '//div[@class="poc_dashboard pbb"]//child::div[@prev_status="red_dot"]//following-sibling::div[@class="clear dx_detail"]//child::div[contains(@class,"dx_row current_yr")]')
    FIRST_PENCIL_ICON = (By.XPATH, '(//div[@class="poc_dashboard pbb"]//child::i)[1]')
    OPEN_POC_BUTTON = (By.XPATH, '(//a[text()="Confirm/Disconfirm"])[1]')
    DX_CODES = (By.XPATH, '//div[@class="code_details col careops-new"]')
