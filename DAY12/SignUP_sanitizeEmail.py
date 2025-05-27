import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox()
driver.maximize_window()
driver.get("https://sanitize-crm.netlify.app/login")
wait= WebDriverWait(driver,10)

signUp= wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Sign Up']")))
driver.execute_script("arguments[0].click()",signUp)

Name= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
Name.send_keys("Alpha Test")

Email= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))
Email.send_keys("fitefi2554@pricegh.com")

Password=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
Password.send_keys("P@$$w0rd")

CheckPolicy= wait.until(EC.presence_of_element_located((By.XPATH,"//button[@role='checkbox']")))
CheckPolicy.click()

SignUP=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
SignUP.click()

time.sleep(7)