# Risk_Quality_CodingTool
Automation framework for Risk &amp; Quality POC using Selenium-Python. Includes modular action functions (Login, OpenPOC, ConfirmHCC, AddDX, Upload Docs, Submit, etc.) and structured Smoke/Regression test suites for scalable, maintainable QA automation.

# Risk_Quality_CodingTool

Risk_Quality_CodingTool is a modular Selenium-Python automation framework designed for validating the Risk & Quality Proof of Concept (POC).  
It follows a clean Page Object + Action Function architecture, enabling scalable test creation for Smoke, Sanity, and Regression suites.

---

## 🚀 Features

- **Modular action-based structure**
  - Login
  - OpenPOC
  - ConfirmHCC
  - DisconfirmHCC
  - AddDX
  - AddDOS
  - AddRenderingProvider
  - DocumentUpload
  - Submit
  - Logout

- **Reusable components** for UI navigation and workflow automation  
- **Customizable test suites** (Smoke, Regression, End-to-End)  
- **Centralized configuration** (URLs, credentials, environment toggles)  
- **Integrated logging & reporting** for validation and debugging  
- **Easy to extend** for future Risk/Quality features

---

📁 Project Structure



<img width="591" height="555" alt="image" src="https://github.com/user-attachments/assets/92e7fb0b-cdc6-4c51-adfc-4d769e368516" />

🧠 Architecture Overview

The framework is organized according to a layered pattern to ensure readability, maintainability, and separation of responsibilities:

1️⃣ Test Layer — testcases/

Contains pytest test modules with functions/classes.

Uses fixtures from conftest.py to obtain page objects and driver.

Tests must not use low-level find_element calls.

Tests interact with page objects such as:

page = RiskPOC(driver)
assert page.some_action_or_check()

2️⃣ Fixture / Orchestration — conftest.py

Creates and configures the WebDriver (e.g., Chrome + options like headless, custom profile).

Provides fixtures for:

Web driver

Page objects (instantiated with driver)

Test data/environment configs

Handles teardown via driver.quit().

Fixtures help abstract repeated setup logic and ensure clean resource management with scopes such as session, module, or function.

3️⃣ Page Layer — pages/*.py

Implements the Page Object Model (POM).

Contains methods representing UI interactions and queries.

Return states/results — no assertions inside page layer.

Uses locator constants from the locator layer.

Typical content in BasePage:

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_visibility(self, locator):
        ...
    def click(self, locator):
        ...
    def send_keys(self, locator, text):
        ...

4️⃣ Locator Layer — pages/locators/*.py

Stores locators as constants with Selenium locators:

ADD_DX_BUTTON = (By.XPATH, "//div[contains(@class,'dx_search') and contains(., '+ Add Dx')]")


Keeps selectors centralized and reusable.

5️⃣ Utils Layer — utils/

Generic reusable helpers for:

Waiting logic

JS execution

Screenshot capture

Retry logic

Logging

Decoupled from test logic for better maintainability.

Utils are stateless where possible and helpers are consumed by page objects and core framework.

6️⃣ TestResource Layer — testresource/

Environment configurations (URLs, credentials), constants, test data.

Browser driver binary (e.g., chromedriver) or driver management logic.

Fixtures can read this layer for environment setup.

7️⃣ Reporting / Artifacts — allure-results/

Collected test artifacts (screenshots, logs).

Used by Allure or other reporting tools to generate reports on test execution.

🚀 Call Sequence (example run)

1️⃣ pytest runner starts
2️⃣ conftest.py instantiates WebDriver → driver fixture
3️⃣ Test receives driver or page object fixture
4️⃣ Test calls page object method
5️⃣ Page method uses locators and helpers (utils.web_utils, BasePage)
6️⃣ WebDriver interacts with browser via ChromeDriver
7️⃣ Test asserts on returned values; on failure, artifact saved to allure-results

📌 Best Practices

✅ Keep locators in locators/*.py only — one locator per constant
✅ Page objects return data/states only (no asserts)
✅ Tests contain assertions and high-level flow logic
✅ Use explicit waits (WebDriverWait) — don’t rely solely on static sleeps
✅ Fixture-driven setup/teardown — avoid manual driver handling in tests
✅ Centralize config & secrets — no hardcoded values
✅ Logging at debug level — avoid prints; use logger
✅ Screenshots on failure for diagnostics

🛠️ Quick Start
# install dependencies
pip install -r requirements.txt

# run tests with pytest
pytest -s -v 

# generate Allure HTML report
allure generate allure-results -o allure-report --clean


