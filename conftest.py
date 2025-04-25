import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_browser(request):
    driver = webdriver.Chrome()  # Use the appropriate WebDriver
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    request.cls.driver = driver
    yield
    driver.quit()