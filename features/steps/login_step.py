from behave import given, when, then
from utiles.driver import get_driver
from pages.login_page import LoginPage
from pages.Inventory_page import HomePage


@given("I am on the Demo Login Page")
def step_login(context):
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()


@when("I fill the account information for account StandardUser into the Username field and the Password field")
def step_login_with_credentials(context):
    context.login_page.login("standard_user", "secret_sauce")


@when("I click the Login Button")
def step_click_login(context):
    context.login_page.click_login()
    assert "inventory.html" in context.driver.current_url, "Valid login credentials fails as inventory.html not found in URL."
    print("[PASS] Login Successfully.")


@then("I am redirected to the Demo Main Page")
def step_confirm_demo(context):
    assert "inventory.html" in context.driver.current_url, "Not redirected to main page."


@then("I verify the App Logo exists")
def step_verify_log(context):
    context.homepage = HomePage(context.driver)
    assert context.homepage.verify_app_logo(),"App logo not visible."
    context.driver.quit()
