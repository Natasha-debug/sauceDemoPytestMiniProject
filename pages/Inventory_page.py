from selenium.webdriver.common.by import By
import json

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    PRODUCTS = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    MENU = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT = (By.CSS_SELECTOR, "#logout_sidebar_link")


    def get_products_with_desc(self):
        products = self.driver.find_elements(*HomePage.PRODUCTS)
        descriptions = self.driver.find_elements(*HomePage.PRODUCT_DESC)

        return [(p.text, d.text) for p, d in zip(products, descriptions)]

    def save_productDetails_to_file(self, filename):
        store_data = self.get_products_with_desc()
        with open(filename, 'w', encoding="utf-8") as f:
            for name, desc in store_data:
                f.write(f"Product: {name}\nDescription: {desc}\n\n")

    def save_productDetails_to_json(self, filename="products.json"):
        products = self.get_products_with_desc()
        data = [{"product_name": p, "description": d} for p, d in products]

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[INFO] Product data saved successfully to {filename}")

    def logout(self):
        self.driver.find_element(*HomePage.MENU).click()
        assert "Login" in self.driver.find_element(*HomePage.LOGOUT).text, "not reached in Login page."
        print("\n[INFO] Successfully reached the Login Page...")

