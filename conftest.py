import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    url = "https://finance.google.com/"
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
