from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

time.sleep(3)

Username= driver.find_element(By.XPATH,"//input[@id='user-name']")
Username.send_keys('performance_glitch_user')

time.sleep(3)
Password= driver.find_element(By.XPATH,"//input[@id='password']")
Password.send_keys('secret_sauce')
