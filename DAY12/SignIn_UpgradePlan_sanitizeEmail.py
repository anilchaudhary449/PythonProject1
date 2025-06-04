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

time.sleep(3)
userPass=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
userPass.send_keys("P@$$w0rd")

LoginBtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
LoginBtn.click()

#upgradePlan
upGradePlan= wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[text()='Upgrade Plan'])[1]")))
upGradePlan.click()

PlanSub= wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[contains(text(),'Upgrade to ')])[1]")))
driver.execute_script("arguments[0].click()", PlanSub)

UpgradeBtn= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Upgrade']")))
driver.execute_script("arguments[0].click()",UpgradeBtn)

driver.switch_to.frame("paddle_frame")
Continue= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Continue']")))
driver.execute_script("arguments[0].click()",Continue)

cardNumber= wait.until(EC.presence_of_element_located((By.ID,"cardNumber")))
cardNumber.send_keys("4242424242424242")

cardName= wait.until(EC.presence_of_element_located((By.ID,"cardHolder")))
cardName.send_keys("Alpha Test")

CardExpiry= wait.until(EC.presence_of_element_located((By.ID,"expiry")))
CardExpiry.send_keys("1230")

CVv= wait.until(EC.presence_of_element_located((By.ID,"cvv")))
CVv.send_keys("345")

SubscribeNow= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Subscribe now']")))
driver.execute_script("arguments[0].click()",SubscribeNow)

driver.quit()