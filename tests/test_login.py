from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url