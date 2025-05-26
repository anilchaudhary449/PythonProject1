import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

DropDown= Select(driver.find_element(By.ID,"dropdown-class-example"))
DropDown.select_by_visible_text("Option1")
time.sleep(3)
DropDown.select_by_index(2)
time.sleep(3)
DropDown.select_by_value("option3")