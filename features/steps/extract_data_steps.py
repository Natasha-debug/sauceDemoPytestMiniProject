from behave import given, when, then
from utiles.driver import get_driver
from pages.login_page import LoginPage
from pages.Inventory_page import HomePage
from utiles.config import PRODUCTS_FILENAME_BEHAVE


@given('I am logged in with valid credentials')
def step_login(context):
    context.driver = get_driver()
    login_page = LoginPage(context.driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in context.driver.current_url, "Login Failed."


@when('I am on the inventory page')
def step_inventory(context):
    context.home_page = HomePage(context.driver)
    assert "inventory.html" in context.driver.current_url, "Not on inventory page."


@then('I extract all product names and descriptions from the page')
def step_extract(context):
    products = context.home_page.get_products_with_desc()

    assert len(products) > 0, "No products found in inventory page."
    context.products = products


@then('I save them to a file')
def step_save(context):
    context.home_page.save_productDetails_to_file(PRODUCTS_FILENAME_BEHAVE)
    context.home_page.save_productDetails_to_json()


@then('I log out')
def step_logout(context):
    context.home_page.logout()


@then('I verify I am on the login page again')
def step_verify(context):
    assert "saucedemo.com" in context.driver.current_url
    context.driver.quit()
