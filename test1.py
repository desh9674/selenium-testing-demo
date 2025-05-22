import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, allure



@allure.title("Google Search Test")
@allure.description("test if google search for SSelenium python' shows results")
def test_google_search():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.duckduckgo.com")
    time.sleep(4)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(4)

    results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
    assert len(results) > 0, "No search results found"
    driver.quit()

