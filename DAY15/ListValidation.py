import time
from selenium import webdriver
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

time.sleep(3)
userPass=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
userPass.send_keys("P@$$w0rd")

LoginBtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
LoginBtn.click()

VerifyEmail= wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='Verify Email']")))
driver.execute_script("arguments[0].click()",VerifyEmail)

ListValidation= wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='List Validation']")))
driver.execute_script("arguments[0].click()",ListValidation)

Addlist= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()=' Add List']")))
driver.execute_script("arguments[0].click()",Addlist)

SwitchToFile= wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Switch to file upload?']")))
driver.execute_script("arguments[0].click()",SwitchToFile)

ListName= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name']")))
ListName.send_keys("TEST")

FileUpload= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
FileUpload.send_keys("C:\\Users\\anilb\\Documents\\TestFile.xlsx")

ValidationType= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='select__value-container select__value-container--is-multi select__value-container--has-value css-1dyz3mf']")))
# driver.execute_script("arguments[0].click()",ValidationType)
ValidationType.click()
ValidationOpt= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__option') and contains(., 'SMTP validation')]")))
driver.execute_script("arguments[0].click()",ValidationOpt)
ValidationType.click()

RunValidation=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
RunValidation.click()



