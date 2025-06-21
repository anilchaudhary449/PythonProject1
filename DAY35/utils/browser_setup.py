# utils/browser_setup.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def get_driver(browser_type):
    if browser_type.lower() == "chrome":
        return webdriver.Chrome(service=ChromeService())
    elif browser_type.lower() == "firefox":
        return webdriver.Firefox(service=FirefoxService())
    else:
        raise ValueError("Unsupported browser type")
