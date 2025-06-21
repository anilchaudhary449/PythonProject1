# test_login.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config_reader import load_properties
from utils.logger import get_logger

logger = get_logger("TestLogin")
config = load_properties("config.properties")

@pytest.mark.usefixtures("setup_driver")
def test_login(setup_driver):
    driver = setup_driver
    wait = WebDriverWait(driver, int(config["explicit_wait"]))

    driver.get(config["base_url"])
    logger.info(f"Opened: {config['base_url']}")

    username = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    username.send_keys(config["username"])
    logger.info("Entered username")

    password = driver.find_element(By.NAME, "password")
    password.send_keys(config["password"])
    logger.info("Entered password")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    logger.info("Clicked login")

    # 🔴 Intentional failure to test screenshot
    assert "Dashboard" in driver.title
