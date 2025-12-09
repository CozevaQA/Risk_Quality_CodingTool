from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def action_click(driver,element):
    try:
        element.click()
    except (ElementNotInteractableException, ElementClickInterceptedException,StaleElementReferenceException):

        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)

def wait_for_page_load(driver,timeout):
    loader_element_class = 'ajax_preloader'
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, loader_element_class)))