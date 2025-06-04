import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox()
driver.maximize_window()
driver.get("https://training.rcvacademy.com/test-automation-practice-page")
wait=WebDriverWait(driver,10)

#scroll iframe into view
iFrame=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='iFrame Example']")))
driver.execute_script("arguments[0].scrollIntoView(true)",iFrame)

#switch to iframe-I
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='RCV Academy eLearning Portal']"))
iframe_AutomationPage=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='AUTOMATION PRACTICE PAGE']")))
iframe_AutomationPage.click()

#CheckBoxes in iframe-I
SeleniumJava= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
SeleniumJava.click()
print("iframe-I, Checkbox:",SeleniumJava.text)

#Js-Popup Alert Boxes in iframe-I
AlertBox= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true)",AlertBox)
AlertBox.click()
alert1=driver.switch_to.alert
print("iframe-I, Alert Box: ",alert1.text)
alert1.accept()

#scroll iframe-II into view
iFrame_II=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='iFrame Example']")))
driver.execute_script("arguments[0].scrollIntoView(true)",iFrame_II)

#switch to iframe-II
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='RCV Academy eLearning Portal']"))
iframe_II_AutomationPage=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='AUTOMATION PRACTICE PAGE']")))
iframe_II_AutomationPage.click()

#CheckBoxes in iframe-II
SeleniumJava_II= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
driver.execute_script("arguments[0].scrollIntoView(true)",SeleniumJava_II)
SeleniumJava_II.click()
print("iframe-II, Checkbox:",SeleniumJava_II.text)

#Js-Popup Alert Boxes in iframe-II
AlertBox_II= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true)",AlertBox_II)
AlertBox_II.click()
alert1=driver.switch_to.alert
print("iframe-II, AlertBox:",alert1.text)
alert1.accept()

driver.switch_to.default_content()

#CheckBoxes
SeleniumJava= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
SeleniumJava.click()
print("Checkbox:",SeleniumJava.text)

#open new browser window
BrowseNewWindow_0= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='myFunctionNewBrowser()']")))
driver.execute_script("arguments[0].scrollIntoView(true)", BrowseNewWindow_0)
BrowseNewWindow_0.click()
print("Browser New Window: ",BrowseNewWindow_0.text)

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
AutomationPage_newBrowser=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='AUTOMATION PRACTICE PAGE']")))
AutomationPage_newBrowser.click()

#CheckBoxes
SeleniumJava= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
SeleniumJava.click()
print("NewWindow_Checkbox:",SeleniumJava.text)

driver.switch_to.window(driver.window_handles[0])

