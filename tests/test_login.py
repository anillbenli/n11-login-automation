from utils.driver_factory import create_driver
from pages.login_page import LoginPage
import time


def _test_open_login_page_and_click_login():
    driver = create_driver()

    login_page = LoginPage(driver)
    login_page.open()

    time.sleep(3)

    login_page.click_login()

    time.sleep(3)

    driver.quit()

def test_email_or_phone_input_accepts_valid_formats():
    from utils.driver_factory import create_driver
    from pages.login_page import LoginPage
    import time

    driver = create_driver()
    page = LoginPage(driver)
    page.open()

    time.sleep(2)

    page.type_email_or_phone("test@example.com")
    value_after_email = page.get_email_or_phone_value()
    assert value_after_email == "test@example.com"

    page.clear_email_or_phone()
    value_after_clear = page.get_email_or_phone_value()
    assert value_after_clear == ""

    page.type_email_or_phone("5551234567")
    value_after_phone = page.get_email_or_phone_value()
    assert value_after_phone == "5551234567"

    driver.quit()

def test_login_fails_with_incorrect_password():
    from utils.driver_factory import create_driver
    from pages.login_page import LoginPage
    import time

    driver = create_driver()
    page = LoginPage(driver)
    page.open()

    time.sleep(3)

    page.type_email_or_phone("anilbenli0644@gmail.com")

    page.click_login()
    time.sleep(3)

    page.type_password("wrong_password")

    page.click_login()
    time.sleep(3)

    assert page.is_login_error_displayed() is True

    time.sleep(5)
    driver.quit()

def test_login_fails_when_fields_are_empty():
    from utils.driver_factory import create_driver
    from pages.login_page import LoginPage
    import time

    driver = create_driver()
    page = LoginPage(driver)
    page.open()

    time.sleep(3)

    page.click_login()
    time.sleep(3)

    assert page.is_empty_fields_error_displayed() is True

    time.sleep(3)
    driver.quit()
