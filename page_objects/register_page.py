from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "customer.firstName")
        self.last_name_input = (By.ID, "customer.lastName")
        self.address_input = (By.ID, "customer.address.street")
        self.city_input = (By.ID, "customer.address.city")
        self.state_input = (By.ID, "customer.address.state")
        self.zip_code_input = (By.ID, "customer.address.zipCode")
        self.phone_input = (By.ID, "customer.phoneNumber")
        self.ssn_input = (By.ID, "customer.ssn")
        self.username_input = (By.ID, "customer.username")
        self.password_input = (By.ID, "customer.password")
        self.confirm_password_input = (By.ID, "repeatedPassword")
        self.register_button = (By.XPATH, "//input[@value='Register']")
        self.success_message = (By.XPATH, "//p[contains(text(), 'Your account was created successfully.')]")

    def navigate_to_register_page(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()

    def fill_registration_form(self, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password, confirm_password):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.state_input).send_keys(state)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.ssn_input).send_keys(ssn)
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    def submit_registration_form(self):
        self.driver.find_element(*self.register_button).click()

    def is_registration_successful(self):
        return self.driver.find_element(*self.success_message).is_displayed()