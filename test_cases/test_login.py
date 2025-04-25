import pytest
from page_objects.login_page import LoginPage
from test_data.test_data import TestData

@pytest.mark.usefixtures("setup_browser")
class TestLogin:

    def test_login(self):
        driver = self.driver
        login_page = LoginPage(driver)

        # Navigate to the base URL
        driver.get(TestData.BASE_URL)

        # Perform login
        login_page.enter_username(TestData.USERNAME)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_login()

        # Verify login success
        assert login_page.is_login_successful(), "Login failed"

        input("Press Enter to close the browser...")