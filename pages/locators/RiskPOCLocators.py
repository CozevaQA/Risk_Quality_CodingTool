from selenium.webdriver.common.by import By

class RiskPOCLocators:

    # -------------------- Existing Locators --------------------
    POC_DX = (
        By.XPATH,
        '//div[@class="dx_code_div gray_background"]//child::div'
    )

    SHOW_DX_BUTTON = (
        By.XPATH,
        '//div[@class="collapse flex"]'
    )

    # -------------------- Dashboard / Structure --------------------
    DASHBOARD = (By.XPATH, "//*[@class='poc_dashboard pbb']")
    POC_BODY = (By.XPATH, "//*[@class='poc_body']")

    # -------------------- Buttons / Actions --------------------
    CONFIRM_DISCONFIRM = (By.XPATH, "//*[contains(text(),'Confirm/Disconfirm')]")
    PRE_REVIEW_REPORT = (By.XPATH, "//*[contains(text(),'Pre-review Report')]")

    # -------------------- Tags --------------------
    RECAPTURE_TAG = (By.XPATH, "//span[contains(text(),'Recapture')]")
    SUSPECT_TAG = (By.XPATH, "//span[contains(text(),'Suspect')]")

    # -------------------- Tooltips (Placeholders – Add real XPaths later) --------------------
    CONFIRM_TOOLTIP = None
    DISCONFIRM_TOOLTIP = None
    NOT_ADDRESSED_TOOLTIP = None

    # -------------------- Add DX Modal --------------------
    ADD_DX_BUTTON = None                      # TODO: Add when XPath/ID provided
    ADD_DX_MODAL_INPUT = (By.ID, "review_dx_input")
    ADD_DX_MODAL_LIST = (By.ID, "ac-dropdown-review_dx_input")

    # -------------------- Notes Section --------------------
    ADD_NOTE_BUTTON = None                    # TODO: update when you get locator
    NOTE_TEXTAREA = (By.ID, "edit-note-field")
    NOTE_SAVE_BUTTON = (By.XPATH, "//a[contains(text(),'Save')]")
    NOTE_SUGGESTIONS_LIST = (By.XPATH, "//ul[@id='ac-dropdown-edit-note-field']")

    # -------------------- DOS / Provider Fields --------------------
    DOS_FIELD = (By.ID, "enc_service_date")
    PROVIDER_FIELD = (By.ID, "provider_name")
    PROVIDER_LIST = (By.XPATH, "//ul[@id='ac-dropdown-provider_name']")

    # -------------------- POC Primary Buttons --------------------
    SAVE_DRAFT = (By.ID, "save_draft")
    SUBMIT = (By.ID, "poc_submit")
    DELETE = (By.ID, "delete_task")

    # -------------------- Alerts / Messages --------------------
    DRUPAL_ALERT = (By.XPATH, "//*[@class='drupal_message_text']")
    AUTOSAVE_STATUS = (By.ID, "last_draft_time")

    # -------------------- Delete Modal --------------------
    DELETE_REASON_INPUT = (
        By.XPATH,
        "//*[contains(text(),'Are you sure you want to delete this task?')]/..//*[@class='input-field']"
    )

    DELETE_MODAL_BUTTON = (
        By.XPATH,
        "//*[contains(text(),'Delete')]"
    )