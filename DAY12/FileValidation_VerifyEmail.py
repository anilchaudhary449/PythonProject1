import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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

VerifyEmail= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='block']")))
driver.execute_script("arguments[0].click()",VerifyEmail)

FileValidation=wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='File Validation']")))
driver.execute_script("arguments[0].click()",FileValidation)

time.sleep(2)
StartUpload= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Upload File']")))
StartUpload.click()

ListName= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name']")))
ListName.send_keys("Test1")

FileUpload= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
FileUpload.send_keys("C:\\Users\\anilb\\Documents\\TestFile.xlsx")

ValidationType= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='basic-multi-select css-b62m3t-container']")))
ValidationType.click()
ValidationOpt= wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select__option') and contains(., 'SMTP validation')]")))
driver.execute_script("arguments[0].click()",ValidationOpt)

ValidationType.click()

RunValidation=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
RunValidation.click()