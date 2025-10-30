import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required")
])
def test_invalid_logins(setup, username, password, expected_error):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(username, password)
    actual_error = login_page.get_error_msg()

    assert actual_error == expected_error, f" Expected '{expected_error}', but got '{actual_error}'"
    print(f"[PASS] Invalid login test passed for username='{username}'")



