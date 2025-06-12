import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/")
wait=WebDriverWait(driver, 10)

#firstStep
Tab= wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Tabs']")))
Tab.click()

time.sleep(3)
Section2= wait.until(EC.presence_of_element_located((By.XPATH,"(//h3[text()='Section 2'])[1]")))
driver.execute_script("arguments[0].click()",Section2)