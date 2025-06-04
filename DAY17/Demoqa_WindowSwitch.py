from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")
wait= WebDriverWait(driver,15)

NewTab= wait.until(EC.element_to_be_clickable((By.ID,"tabButton")))
NewTab.click()
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])

NewWindow= wait.until(EC.element_to_be_clickable((By.ID,"windowButton")))
NewWindow.click()
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])

NewWindowMessage= wait.until(EC.element_to_be_clickable((By.ID,"messageWindowButton")))
NewWindowMessage.click()
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])