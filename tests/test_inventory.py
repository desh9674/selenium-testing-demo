from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_items_visible_after_login(driver):
    # Login first
    login = LoginPage(driver)
    login.open()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # Inventory Page checks
    inventory = InventoryPage(driver)
    assert "Products" in inventory.get_title()
    assert inventory.get_item_count() > 0
