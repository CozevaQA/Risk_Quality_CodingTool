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

## 📁 Project Structure (Proposed)

DETAILED LAYER RESPONSIBILITIES & INTERACTIONS (technical)
#
# 1) Test Runner / Test Layer (testcases/)
#    - Files: test_poc_launch.py, other test modules
#    - Responsibility:
#       * Define test cases (pytest functions or classes).
#       * Use fixtures (from conftest.py) to get driver / page objects.
#       * Perform assertions on page layer return values.
#    - Interaction:
#       test -> uses page object methods (pages.RiskPOC.RiskPOCPage.some_method())
#       test should NOT contain low-level find_element calls.
#
# 2) Fixture / Orchestration (conftest.py)
#    - Files: conftest.py
#    - Responsibility:
#       * Instantiate WebDriver (using chromedriver from testresource).
#       * Configure browser profile, options (headless, user-data-dir).
#       * Create and provide Page objects (page = RiskPOC(driver)).
#       * Implement teardown (driver.quit()) and session/module/function scoping.
#    - Interaction:
#       conftest provides fixtures to tests and can initialize common data from testresource.
#
# 3) Page Layer (pages/*.py)
#    - Files: BasePage.py, PatientDashboard.py, RiskPOC.py
#    - Responsibility:
#       * Implement Page Object Model (POM): methods that represent user actions and queries.
#       * Return elements or boolean checks (e.g., is_visible_and_displayed).
#       * Avoid assertions here; return values consumed by tests.
#    - Typical contents of BasePage:
#       * driver reference
#       * wait helpers (WebDriverWait wrappers)
#       * common interaction helpers (click, send_keys, scroll_into_view)
#       * the `is_visible_and_displayed(locator)` used everywhere
#
# 4) Locator Layer (pages/locators/*.py)
#    - Files: RiskPOCLocators.py, PatientDashboardLocators.py
#    - Responsibility:
#       * Centralize element locators (By.XPATH, By.CSS_SELECTOR, etc.)
#       * Keep locators as simple, robust, single-responsibility constants
#       * Example: ADD_DX_BUTTON = (By.XPATH, "//div[contains(@class,'dx_search') and contains(., '+ Add Dx')]")
#    - Interaction:
#       Page methods import RiskPOCLocators and use the locator constants with BasePage helpers.
#
# 5) Utils Layer (utils/)
#    - Files: common_utils.py, web_utils.py
#    - Responsibility:
#       * Place generic utilities that are reused across pages/tests:
#            - DOM helpers, JS executors, file upload, waits, retry logic
#            - Logging wrappers, screenshots on failure
#       * Keep these functions pure (no direct test assertions) so they can be reused.
#    - Interaction:
#       BasePage and Page classes call utilities here. Tests rarely call utils directly.
#
# 6) TestResource Layer (testresource/)
#    - Files: chromedriver.exe, constants.py, environment.py, testdata.py
#    - Responsibility:
#       * Environment configuration (urls, credentials), constants used across tests
#       * Test data providers (fixtures or JSON reading)
#       * Driver binaries (chromedriver) or code to download/manage driver
#    - Interaction:
#       conftest reads environment/testdata to configure test runs.
#
# 7) Reporting / Artifacts
#    - Location: allure-results/ (as shown)
#    - Responsibility:
#       * Allure / HTML reports and screenshots
#       * Tests or hooks (pytest hooks in conftest) should write artifacts here on failure.
#
####################################################################################################
#
# CALL SEQUENCE (example single test run)
#
# conftest.py (session fixture) creates WebDriver --> returns driver fixture
#    ↓
# test_poc_launch.py receives driver (or a page fixture created in conftest)
#    ↓
# test calls page = RiskPOC(driver) / uses fixture page
#    ↓
# page.method() uses BasePage.wait + RiskPOCLocators.ADD_DX_BUTTON
#    ↓
# BasePage uses utils.web_utils.wait_for_element(locator)
#    ↓
# WebDriver interacts with browser (chromedriver.exe)
#    ↓
# Test asserts on return values; on failure screenshot/save logs into allure-results
#
####################################################################################################
#
# BEST PRACTICES / RULES YOU SHOULD FOLLOW (technical, 100% correct)
#
# - Keep locators out of page logic: one locator per constant in locators/*.py
# - Page objects expose behavior (actions) or queries (is_visible, get_text). Avoid asserts inside pages.
# - Tests contain assertions only. This separation keeps tests readable and maintainable.
# - Use explicit waits in BasePage (WebDriverWait) and expose small, well-named helpers:
#     * wait_for_visibility(locator, timeout=10)
#     * wait_for_clickable(locator, timeout=10)
#     * is_visible_and_displayed(locator)  # returns boolean, safe for page dictionary
# - Use fixtures to manage driver lifecycle and to inject test data/env configs.
# - Centralize test constants & credentials in testresource/environment.py (DO NOT hardcode secrets).
# - Keep utils stateless when possible. If stateful, document it clearly.
# - Log at debug level inside utils and BasePage; do not print in production tests.
#
####################################################################################################
#
# QUICK ASCII DIAGRAM (compact)
#
#   [pytest runner]
#        |
#    conftest.py --(fixtures)-> provides driver, env, page instances
#        |
#    testcases/*.py  (uses page objects)
#        |
#    pages/*.py  <------ uses ------ pages/locators/*.py
#        |                                ^
#        |                                |
#   BasePage, web_utils.py  <-------------+
#        |
#   selenium webdriver <--> chromedriver.exe
#        |
#   browser
#



