from selenium.webdriver.common.by import By
from selenium import webdriver
import time


driver= webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

F_Name= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input')
F_Name.send_keys('Anil')

L_Name= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[4]/input')
L_Name.send_keys('Chaudhary')

Email= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div[2]/input')
Email.send_keys('abc@gmail.com')

#Gender= driver.find_element(By.PARTIAL_LINK_TEXT,'Male')
#Gender.click()

Mobile_number= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/input')
Mobile_number.send_keys('98765433201')

DOB1= driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div/div/input')
DOB1.click()

DOB2=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]')
DOB2.click()

Subject= driver.find_element(By.CSS_SELECTOR,'#subjectsInput')
Subject.send_keys('Maths')
time.sleep(2)
Subject.send_keys('\ue007')

Hobbies= driver.find_element(By.ID,'hobbies-checkbox-1')
driver.execute_script("arguments[0].click();", Hobbies)

Current_Address= driver.find_element(By.ID,'currentAddress')
Current_Address.send_keys('Test Current Address')

# state_dropdown= driver.find_element(By.ID,'state')
# driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
# time.sleep(2)
# driver.execute_script("arguments[0].click();", state_dropdown)

Image=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[8]/div[2]/div/input')
Image.send_keys('C:\\Users\\anilb\\OneDrive\\Desktop\\WhatsApp Image 2025-04-28 at 17.10.36_e705cbec.jpg')

submit_btn= driver.find_element(By.ID,'submit')
submit_btn.click()