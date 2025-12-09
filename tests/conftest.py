import os
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from testresource.environment import *
from testresource.environment import (
    username,
    password,
    submit,
    reason_textbox
)
from utils import common_utils
from utils import web_utils as webfunctions

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "edge"],
        help="Browser to run tests on",
    )
@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    # 👉 Check if profile folder exists, else create it
    if not os.path.exists(CHROME_PROFILE):
        os.makedirs(CHROME_PROFILE)
        print(f"Created Chrome profile directory: {CHROME_PROFILE}")
    else:
        print(f"Using existing Chrome profile directory: {CHROME_PROFILE}")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        service = Service(executable_path="testresource/chromedriver.exe")
        # 👉 Chrome profile setup
        options.add_argument(f"--user-data-dir={CHROME_PROFILE}")
        options.add_argument("--profile-directory=Default")     # or Profile 1

        drv = webdriver.Chrome(
            service=service,
            options=options,
        )

    elif browser == "edge":
        options = webdriver.EdgeOptions()

        # 👉 Edge profile setup
        edge_profile_path = os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\User Data")
        options.add_argument(f"--user-data-dir={edge_profile_path}")
        options.add_argument("--profile-directory=Default")     # or Profile 1

        drv = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options,
        )

    drv.maximize_window()
    yield drv
    # drv.quit()

#
@pytest.fixture(scope="session", autouse=True)
def login_once(driver):
    """
    Runs ONCE before any test (session scoped) and logs in.
    All tests will see an already logged-in browser.
    """
    # Go to login page
    driver.get(LOGIN_URL)
    driver.maximize_window()

    wait= WebDriverWait(driver, 120)
    #  Enter username
    uname_el = wait.until(EC.presence_of_element_located((By.ID, username)))
    uname_el.clear()
    uname_el.send_keys(common_utils.decode_base64(USERNAME))

    #  Enter password
    pwd_el = driver.find_element(By.ID, password)
    pwd_el.clear()
    pwd_el.send_keys(common_utils.decode_base64(PASSWORD))

    #  Submit login (first submit)
    submit_el = wait.until(EC.element_to_be_clickable((By.ID, submit)))
    submit_el.click()

    # --------------- ALWAYS ENTER REASON ---------------- #

    #  Wait for reason textbox
    reason_el = wait.until(
        EC.presence_of_element_located((By.XPATH, reason_textbox))
    )

    #  Enter reason
    actions = ActionChains(driver)
    actions.move_to_element(reason_el).click().send_keys(REASON).perform()

    # Submit again (second submit)
    submit_el2 = wait.until(EC.element_to_be_clickable((By.ID, submit)))
    submit_el2.click()
    webfunctions.wait_for_page_load(driver, 120)
