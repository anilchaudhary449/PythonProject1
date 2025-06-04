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

time.sleep(9)
Alpha_account= wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='lucide lucide-chevron-down']")))
Alpha_account.click()

time.sleep(3)
Settings= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Settings']")))
driver.execute_script("arguments[0].click()",Settings)

Team= wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='Team']")))
driver.execute_script("arguments[0].click()",Team)

addUser= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()=' New User']")))
driver.execute_script("arguments[0].click()",addUser)

firstName= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='firstname']")))
lastName= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='lastname']")))
email= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))

firstName.send_keys("Test")
lastName.send_keys("Tester")
email.send_keys("test@abd.com")

Role= wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Select Role']")))
driver.execute_script("arguments[0].click()",Role)

option= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='developer']")))
driver.execute_script("arguments[0].click()",option)

Submit= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Send Invitation']")))
Submit.click()