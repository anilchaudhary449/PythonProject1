from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://demoqa.com")
driver.maximize_window()
wait=WebDriverWait(driver,10)

Alert= wait.until(EC.presence_of_element_located((By.XPATH,"//h5[text()='Alerts, Frame & Windows']")))
driver.execute_script("arguments[0].click()",Alert)

Frames=wait.until(EC.element_to_be_clickable((By.ID,"//span[text()='Frames']")))
Frames.click()