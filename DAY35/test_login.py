# test_login.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config_reader import load_properties
from utils.browser_setup import get_driver
from utils.logger import get_logger

logger = get_logger("TestLogin")
config = load_properties("config.properties")

@pytest.mark.smoke
def test_login():
    logger.info("Starting test_login")
    driver = get_driver(config["browser"])
    wait = WebDriverWait(driver, int(config["explicit_wait"]))

    try:
        driver.get(config["base_url"])
        logger.info(f"Opened URL: {config['base_url']}")

        username = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        username.send_keys(config["username"])
        logger.info("Entered username")

        password = driver.find_element(By.NAME, "password")
        password.send_keys(config["password"])
        logger.info("Entered password")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        logger.info("Clicked login button")

        # Add meaningful check after login, like dashboard visibility
        assert "dashboard" in driver.current_url or "Sanitize  Email" in driver.title

    except Exception as e:
        logger.error(f"Test failed: {e}")
        pytest.fail(str(e))

    finally:
        driver.quit()
        logger.info("Browser closed")
