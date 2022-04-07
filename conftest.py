import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver_path = "/Users/Heisenberg/.wdm/drivers/chromedriver/mac64/100.0.4896.60/chromedriver"

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()
