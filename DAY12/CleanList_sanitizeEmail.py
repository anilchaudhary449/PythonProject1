import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox()
driver.maximize_window()
driver.get("https://sanitize-crm.netlify.app/login")
wait= WebDriverWait(driver,15)

userName=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))
userName.send_keys("fitefi2554@pricegh.com")

userPass=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
userPass.send_keys("P@$$w0rd")

LoginBtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
LoginBtn.click()

cleanList=wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='Clean List']")))
driver.execute_script("arguments[0].click()",cleanList)

Clean_List= wait.until(EC.presence_of_element_located((By.XPATH,"(//button[text()='Clean List'])[1]")))
driver.execute_script("arguments[0].click()",Clean_List)

ValidationType= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='basic-multi-select css-b62m3t-container']")))
ValidationType.click()
ValidationOpt= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__option') and contains(., 'SMTP validation')]")))
driver.execute_script("arguments[0].click()",ValidationOpt)

ValidationType.click()

clean_List=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
driver.execute_script("arguments[0].scrollIntoView(true)",clean_List)
clean_List.click()
