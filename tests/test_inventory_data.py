from pages.login_page import LoginPage
from pages.Inventory_page import HomePage
from utiles.config import PRODUCTS_FILENAME


def test_inventory_data(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url, "Login Failed."

    inventory_page = HomePage(driver)
    products = inventory_page.get_products_with_desc()

    assert len(products) > 0, "No products found in inventory page."

    inventory_page.save_productDetails_to_file(PRODUCTS_FILENAME)
    inventory_page.save_productDetails_to_json()

    inventory_page.logout()
    assert "saucedemo.com" in driver.current_url, "not reached in Login page."
    print("\n[INFO] Successfully reached the Login Page at end...")




