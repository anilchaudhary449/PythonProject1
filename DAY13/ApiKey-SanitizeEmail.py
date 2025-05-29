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

ApiKey= wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='API Key']")))
ApiKey.click()

GenerateNewKey= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Generate New Key']")))
driver.execute_script("arguments[0].click()",GenerateNewKey)

API_Name= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='name']")))
API_Name.send_keys("Test")

Note= wait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@name='notes']")))
Note.send_keys("This is Note.")

stLimit= wait.until(EC.presence_of_element_located((By.XPATH,"//button[@value='NO']")))
stLimit.click()

AuthorizedDomain=wait.until(EC.presence_of_element_located((By.ID,"domain")))
AuthorizedDomain.send_keys("test.com")

AddBtn=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Add']")))
driver.execute_script("arguments[0].click()",AddBtn)

GenerateKey=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
driver.execute_script("arguments[0].click()",GenerateKey)