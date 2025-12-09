
from pages.Patient_Dashboard import Patient_Dashboard
from pages.Risk_POC import Risk_POC
from testresource import testdata,environment

def test_poc_launch(driver, timeout=20):
    patient = Patient_Dashboard(driver, timeout, testdata.patient_cozeva_id)

    assert patient.open_patient_dashboard(environment.BASE_URL), "Patient dashboard failed to open"

    risk_poc = patient.open_poc()
    assert risk_poc, "open_poc() returned False (POC did not open)"

    # Now safe to call is_page_loaded(); your method returns self on success
    assert risk_poc.is_page_loaded() is risk_poc