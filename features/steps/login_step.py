from behave import given, when, then
from utiles.driver import get_driver
from pages.login_page import LoginPage
from pages.Inventory_page import HomePage


@given("I am on the Demo Login Page")
def login(context):
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()


@when("When I fill the account information for account StandardUser into the Username field and the Password field And I click the Login Button")
def login_with_credentials(context):
    context.login_page.login("standard_user", "secret_sauce")


@then("And I click the Login Button")
def click_login(context):
    context.login_page.click_login()
    assert "inventory.html" in context.driver.current_url, "Valid login credentials fails as inventory.html not found in URL."
    print("[PASS] Login Successfully.")


@then("Then I am redirected to the Demo Main Page")
def confirm_demo(context):
    assert "inventory.html" in context.driver.current_url, "Not redirected to main page."


@then("And I verify the App Logo exists")
def verify_log(context):
    context.homepage = HomePage(context.driver)
    assert context.homepage.verify_app_logo(),"App logo not visible."
    context.driver.quit()
