import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://authorized-partner.netlify.app/register/")
driver.maximize_window()
time.sleep(3)
driver.close()