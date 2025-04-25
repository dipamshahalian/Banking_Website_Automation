import pytest
from page_objects.register_page import RegisterPage
from test_data.test_data import TestData
@pytest.mark.usefixtures("setup_browser")
class TestRegisterAccount:

    def test_register_account(self):
        driver = self.driver
        register_page = RegisterPage(driver)

        # Navigate to the registration page
        register_page.navigate_to_register_page()

        # Fill in the registration form using data from TestData
        register_page.fill_registration_form(
            first_name=TestData.FIRST_NAME,
            last_name=TestData.LAST_NAME,
            address=TestData.ADDRESS,
            city=TestData.CITY,
            state=TestData.STATE,
            zip_code=TestData.ZIP_CODE,
            phone=TestData.PHONE,
            ssn=TestData.SSN,
            username=TestData.USERNAME,
            password=TestData.PASSWORD,
            confirm_password=TestData.CONFIRM_PASSWORD
        )

        # Submit the form
        register_page.submit_registration_form()

        # Verify successful registration
        assert register_page.is_registration_successful(), "Account registration failed"

        input("Press Enter to close the browser...")