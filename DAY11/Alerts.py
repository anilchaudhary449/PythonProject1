import time
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

AlertBtn= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Alerts']")))
AlertBtn.click()

ClickMe1= wait.until(EC.element_to_be_clickable((By.ID,"alertButton")))
driver.execute_script("arguments[0].click()",ClickMe1)
alert1= driver.switch_to.alert
print(alert1.text)
alert1.accept()

timerAlert= wait.until(EC.element_to_be_clickable((By.ID,"timerAlertButton")))
timerAlert.click()
time.sleep(6)
alert2=driver.switch_to.alert
print(alert2.text)
alert2.accept()

confirmAlert=wait.until(EC.element_to_be_clickable((By.ID,"confirmButton")))
confirmAlert.click()
alert3=driver.switch_to.alert
print("Confirmation Alert:",alert3.text)
# alert3.accept()
alert3.dismiss()

promptAlert=wait.until(EC.element_to_be_clickable((By.ID,"promptButton")))
promptAlert.click()
alert4=driver.switch_to.alert
print("Prompt Alert:",alert4.text)
alert4.send_keys("Test")
alert4.accept()
# alert4.dismiss()
driver.quit()