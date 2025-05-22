from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.title = (By.CLASS_NAME, "title")

    def get_item_count(self):
        return len(self.driver.find_elements(*self.inventory_items))

    def get_title(self):
        return self.driver.find_element(*self.title).text
