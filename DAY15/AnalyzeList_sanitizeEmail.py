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

AnalyzeList= wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='Analyze List']")))
driver.execute_script("arguments[0].click()",AnalyzeList)

time.sleep(2)
UploadFile= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Upload File']")))
driver.execute_script("arguments[0].click()",UploadFile)

time.sleep(2)
ListName= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name']")))
ListName.send_keys("Test1")

FileUpload= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='file']")))
FileUpload.send_keys("C:\\Users\\anilb\\Documents\\TestFile.xlsx")

time.sleep(4)
AnalyzeBtn= wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
driver.execute_script("arguments[0].click()",AnalyzeBtn)

time.sleep(5)
driver.quit()