import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
wait=WebDriverWait(driver,10)
actions=ActionChains(driver)
driver.get("https://training.rcvacademy.com/test-automation-practice-page")