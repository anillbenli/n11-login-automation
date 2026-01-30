from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.url = "https://www.n11.com/giris-yap"

        self.login_button = (
            By.CSS_SELECTOR,
            "#app > div.content-area > div > div.default-tab > div:nth-child(2) > button"
        )
        
        self.email_phone_input = (By.CSS_SELECTOR, "#email")
        
        self.password_input = (By.CSS_SELECTOR, "#password")
        
        self.login_error_message = (
            By.CSS_SELECTOR,
            "#app > div.content-area > div > div.default-tab > div:nth-child(2) > div.login-error-content > span"
        )

        self.empty_fields_error = (
            By.CSS_SELECTOR,
            "#app > div.content-area > div > div.default-tab > div:nth-child(2) > div:nth-child(1) > span"
        )



    def open(self):
        self.driver.get(self.url)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def type_email_or_phone(self, text: str):
        el = self.driver.find_element(*self.email_phone_input)
        el.clear()
        el.send_keys(text)

    def clear_email_or_phone(self):
        from selenium.webdriver.common.keys import Keys

        el = self.driver.find_element(*self.email_phone_input)
        el.click()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.BACKSPACE)

    def get_email_or_phone_value(self) -> str:
        el = self.driver.find_element(*self.email_phone_input)
        return el.get_attribute("value")
    
    def type_password(self, text: str):
        el = self.driver.find_element(*self.password_input)
        el.clear()
        el.send_keys(text)

    def is_login_error_displayed(self) -> bool:
        try:
            el = self.driver.find_element(*self.login_error_message)
            return el.is_displayed()
        except:
            return False

    def is_empty_fields_error_displayed(self) -> bool:
        try:
            el = self.driver.find_element(*self.empty_fields_error)
            return el.is_displayed()
        except:
            return False
