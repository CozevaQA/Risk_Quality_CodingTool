from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import web_utils as webfunctions
from pages.BasePage import BasePage
from pages.locators.RiskPOCLocators import RiskPOCLocators


class Risk_POC(BasePage):

    def is_page_loaded(self):
        """
        Waits for the necessary elements on the POC page to confirm it loaded.
        Returns self for chaining.
        """

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(RiskPOCLocators.POC_DX)
        )
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(RiskPOCLocators.SHOW_DX_BUTTON)
        )

        return self

    def RecaptureConfirm(self):
        try:
            # Wait for POC body to be present
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            # find the recapture tag
            tag_el = self.driver.find_element(*RiskPOCLocators.RECAPTURE_TAG)

            # ensure the tooltip locator is defined
            if not RiskPOCLocators.CONFIRM_TOOLTIP:
                raise ValueError("CONFIRM_TOOLTIP locator is not defined in RiskPOCLocators")

            # find and click the confirm tooltip inside the tag
            tooltip_el = tag_el.find_element(*RiskPOCLocators.CONFIRM_TOOLTIP)
            try:
                webfunctions.action_click(self.driver, tooltip_el)
            except Exception:
                tooltip_el.click()

            print("Recapture Confirmed Successfully.")
        except Exception as e:
            print("Recapture Confirm Failed:", e)

    def RecaptureDisconfirm(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            tag_el = self.driver.find_element(*RiskPOCLocators.RECAPTURE_TAG)

            if not RiskPOCLocators.DISCONFIRM_TOOLTIP:
                raise ValueError("DISCONFIRM_TOOLTIP locator is not defined in RiskPOCLocators")

            tooltip_el = tag_el.find_element(*RiskPOCLocators.DISCONFIRM_TOOLTIP)
            try:
                webfunctions.action_click(self.driver, tooltip_el)
            except Exception:
                tooltip_el.click()

            print("Recapture Disconfirmed Successfully.")
        except Exception as e:
            print("Recapture Disconfirm Failed:", e)

    def RecaptureNotAddressed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            tag_el = self.driver.find_element(*RiskPOCLocators.RECAPTURE_TAG)

            if not RiskPOCLocators.NOT_ADDRESSED_TOOLTIP:
                raise ValueError("NOT_ADDRESSED_TOOLTIP locator is not defined in RiskPOCLocators")

            tooltip_el = tag_el.find_element(*RiskPOCLocators.NOT_ADDRESSED_TOOLTIP)
            try:
                webfunctions.action_click(self.driver, tooltip_el)
            except Exception:
                tooltip_el.click()

            print("Recapture Marked as Not Addressed Successfully.")
        except Exception as e:
            print("Recapture Not Addressed Failed:", e)

    def SuspectConfirm(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            tag_el = self.driver.find_element(*RiskPOCLocators.SUSPECT_TAG)

            if not RiskPOCLocators.CONFIRM_TOOLTIP:
                raise ValueError("CONFIRM_TOOLTIP locator is not defined in RiskPOCLocators")

            tooltip_el = tag_el.find_element(*RiskPOCLocators.CONFIRM_TOOLTIP)
            try:
                webfunctions.action_click(self.driver, tooltip_el)
            except Exception:
                tooltip_el.click()

            print("Suspect Confirmed Successfully.")
        except Exception as e:
            print("Suspect Confirm Failed:", e)

    def SuspectDisconfirm(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            tag_el = self.driver.find_element(*RiskPOCLocators.SUSPECT_TAG)

            if not RiskPOCLocators.DISCONFIRM_TOOLTIP:
                raise ValueError("DISCONFIRM_TOOLTIP locator is not defined in RiskPOCLocators")

            tooltip_el = tag_el.find_element(*RiskPOCLocators.DISCONFIRM_TOOLTIP)
            try:
                webfunctions.action_click(self.driver, tooltip_el)
            except Exception:
                tooltip_el.click()

            print("Suspect Disconfirmed Successfully.")
        except Exception as e:
            print("Suspect Disconfirm Failed:", e)

    def SuspectNotAddressed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            tag_el = self.driver.find_element(*RiskPOCLocators.SUSPECT_TAG)

            if not RiskPOCLocators.NOT_ADDRESSED_TOOLTIP:
                raise ValueError("NOT_ADDRESSED_TOOLTIP locator is not defined in RiskPOCLocators")

            tooltip_el = tag_el.find_element(*RiskPOCLocators.NOT_ADDRESSED_TOOLTIP)
            try:
                webfunctions.action_click(self.driver, tooltip_el)
            except Exception:
                tooltip_el.click()

            print("Suspect Marked as Not Addressed Successfully.")
        except Exception as e:
            print("Suspect Not Addressed Failed:", e)

    def AddDiagnosis(self, data):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            if not RiskPOCLocators.ADD_DX_BUTTON:
                raise ValueError("ADD_DX_BUTTON locator is not defined in RiskPOCLocators")

            # open add diagnosis modal
            add_btn = self.driver.find_element(*RiskPOCLocators.ADD_DX_BUTTON)
            try:
                webfunctions.action_click(self.driver, add_btn)
            except Exception:
                add_btn.click()
            print("Add Diagnosis Button Clicked Successfully.")

            # type diagnosis code and pick from the suggestion list
            self.driver.find_element(*RiskPOCLocators.ADD_DX_MODAL_INPUT).send_keys(data.dx_code)

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.ADD_DX_MODAL_LIST))
            suggestions = self.driver.find_element(*RiskPOCLocators.ADD_DX_MODAL_LIST).find_elements(By.TAG_NAME, "li")
            if len(suggestions) > 1:
                suggestions[1].click()
            else:
                suggestions[0].click()
            print("Diagnosis Added Successfully.")
        except Exception as e:
            print("Add Diagnosis Failed:", e)

    def AddNote(self, data):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            if not RiskPOCLocators.ADD_NOTE_BUTTON:
                raise ValueError("ADD_NOTE_BUTTON locator is not defined in RiskPOCLocators")

            add_note_btn = self.driver.find_element(*RiskPOCLocators.ADD_NOTE_BUTTON)
            try:
                webfunctions.action_click(self.driver, add_note_btn)
            except Exception:
                add_note_btn.click()
            print("Add Note Button Clicked Successfully.")

            self.driver.find_element(*RiskPOCLocators.NOTE_TEXTAREA).send_keys(data.note)

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.NOTE_SUGGESTIONS_LIST))
            suggestions = self.driver.find_element(*RiskPOCLocators.NOTE_SUGGESTIONS_LIST).find_elements(By.TAG_NAME,
                                                                                                         "li")
            if len(suggestions) > 1:
                suggestions[1].click()
            else:
                suggestions[0].click()

            self.driver.find_element(*RiskPOCLocators.NOTE_SAVE_BUTTON).click()
            print("Note Added Successfully.")
        except Exception as e:
            print("Add Note Failed:", e)

    def SetDOS(self, data):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))
            dos_field = self.driver.find_element(*RiskPOCLocators.DOS_FIELD)
            dos_field.clear()
            dos_field.send_keys(data.dos_field)
            print("Date of Service Set Successfully.")
        except Exception as e:
            print("Set Date of Service Failed:", e)

    def SetProvider(self, data):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))

            provider_field = self.driver.find_element(*RiskPOCLocators.PROVIDER_FIELD)
            provider_field.clear()
            provider_field.send_keys(data.provider_name)

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.PROVIDER_LIST))
            provider_items = self.driver.find_element(*RiskPOCLocators.PROVIDER_LIST).find_elements(By.TAG_NAME, "li")
            if len(provider_items) > 1:
                provider_items[1].click()
            else:
                provider_items[0].click()

            print("Provider Set Successfully.")
        except Exception as e:
            print("Set Provider Failed:", e)

    def SaveDraftPOC(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))
            self.driver.find_element(*RiskPOCLocators.SAVE_DRAFT).click()

            # read notification (drupal alert)
            notif = self.driver.find_element(*RiskPOCLocators.DRUPAL_ALERT).text
            print("Notification:", notif)

            if "changes have been successfully saved" in notif:
                time_text = self.driver.find_element(*RiskPOCLocators.AUTOSAVE_STATUS).text
                print("Autosave Time Updated Successfully:", time_text)
            else:
                print("Draft Save Failed:", notif)

            print("POC Draft Saved Successfully.")
        except Exception as e:
            print("POC Draft Save Failed:", e)

    def SubmitPOC(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))
            self.driver.find_element(*RiskPOCLocators.SUBMIT).click()

            notif = self.driver.find_element(*RiskPOCLocators.DRUPAL_ALERT).text
            print("Notification:", notif)

            if "has been created" in notif:
                print("POC Submitted Successfully.")
            else:
                print("POC Submission Failed:", notif)
        except Exception as e:
            print("POC Submission Failed:", e)

    def DeletePOC(self, data):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.POC_BODY))
            self.driver.find_element(*RiskPOCLocators.DELETE).click()

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.DELETE_REASON_INPUT))
            self.driver.find_element(*RiskPOCLocators.DELETE_REASON_INPUT).send_keys(data.delete_reason)
            self.driver.find_element(*RiskPOCLocators.DELETE_MODAL_BUTTON).click()

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RiskPOCLocators.DRUPAL_ALERT))
            notif = self.driver.find_element(*RiskPOCLocators.DRUPAL_ALERT).text
            print("Notification:", notif)

            if "successfully deleted" in notif:
                print("POC Deleted Successfully.")
            else:
                print("POC Deletion Failed:", notif)
        except Exception as e:
            print("POC Deletion Failed:", e)