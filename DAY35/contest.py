# conftest.py

import pytest
import os
from config_reader import load_properties
from utils.browser_setup import get_driver
from email_utils import send_email_on_failure

def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)

    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver_instance", None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(screenshot_path))
                rep.extra = extra

            # ✅ Send email with screenshot
            subject = f"❌ Selenium Test Failed: {item.name}"
            body = f"The test '{item.name}' failed.\nSee attached screenshot."
            send_email_on_failure(subject, body, to_email="receiver_email@gmail.com", attachment_path=screenshot_path)

@pytest.fixture(scope="function")
def setup_driver(request):
    config = load_properties("config.properties")
    driver = get_driver(config["browser"])
    driver.maximize_window()

    request.node.driver_instance = driver
    yield driver

    driver.quit()
