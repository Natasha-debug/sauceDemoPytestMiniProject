from pages.login_page import LoginPage


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    login_page.click_login()

    assert "inventory.html" in driver.current_url, "Valid login credentials fails as inventory.html not found in URL."
    print("[PASS] Login Successfully.")



