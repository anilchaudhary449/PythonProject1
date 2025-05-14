import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")
driver.maximize_window()

time.sleep(4)
Bank_Manager_LogIn= driver.find_element(By.XPATH,"//button[text()='Bank Manager Login']")
Bank_Manager_LogIn.click()

time.sleep(4)
Home_btn= driver.find_element(By.XPATH,"//button[text()='Home']")
Home_btn.click()

time.sleep(4)
Customer_LogIn= driver.find_element(By.XPATH,"//button[text()='Customer Login']")
Customer_LogIn.click()

time.sleep(4)
Select_Name= driver.find_element(By.XPATH,"//option[text()='---Your Name---']")
Select_Name.click()

time.sleep(4)
Cust_Harry= driver.find_element(By.XPATH,"//option[text()='Harry Potter']")
Cust_Harry.click()

time.sleep(4)
Login= driver.find_element(By.XPATH,"//button[text()='Login']")
Login.click()

time.sleep(4)
Account_Number= driver.find_element(By.XPATH,"//option[text()='1005']")
Account_Number.click()

time.sleep(4)
Logout= driver.find_element(By.XPATH,"//button[text()='Logout']")
Logout.click()

time.sleep(4)
Home_btn= driver.find_element(By.XPATH,"//button[text()='Home']")
Home_btn.click()

time.sleep(5)
driver.quit()

