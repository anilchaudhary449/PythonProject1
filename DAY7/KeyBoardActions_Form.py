import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com")

actions=ActionChains(driver)

driver.implicitly_wait(10)

Form= driver.find_element(By.XPATH,"//h5[text()='Forms']")
driver.execute_script("arguments[0].click()",Form)

PracticeForm= driver.find_element(By.XPATH,"//span[text()='Practice Form']")
driver.execute_script("arguments[0].click()",PracticeForm)

# firstName
actions.click(driver.find_element(By.ID,"firstName")).send_keys("Tester1").send_keys(Keys.TAB).perform()

#lastname
actions.send_keys("Tester2").send_keys(Keys.TAB).perform()

#email
actions.send_keys("tester@gmail.com").send_keys(Keys.TAB).perform()

#close
actions.key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()

#gender
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.SPACE).send_keys(Keys.TAB).perform()

#mobileNumber
actions.send_keys("9876543210").send_keys(Keys.TAB).perform()

#DateOfBirth
actions.key_down(Keys.TAB).send_keys(Keys.ARROW_DOWN).key_up(Keys.TAB).send_keys(Keys.ENTER).perform()

#subjects
SubjectBtn= driver.find_element(By.ID,"subjectsInput")
driver.execute_script("arguments[0].click()",SubjectBtn)
SubjectBtn.send_keys("M")

SubOpt= driver.find_element(By.XPATH,"//div[text()='Chemistry']")
SubOpt.click()

driver.execute_script("window.scrollBy(0, 500);") #scrollWindow

#hobbies
actions.send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.SPACE).perform()

#picture
upload=driver.find_element(By.ID,"uploadPicture")
upload.send_keys("C:\\Users\\anilb\\Downloads\\Screenshot 2025-05-19 223237.png")

#address
actions.click(driver.find_element(By.ID,"currentAddress")).send_keys("abc").send_keys(Keys.TAB).perform()

#selectState
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()

#selectCity
actions.send_keys(Keys.TAB+Keys.ARROW_DOWN+Keys.TAB).perform()

#submit
actions.send_keys(Keys.ENTER).perform()

time.sleep(5)
#Close
actions.send_keys(Keys.ESCAPE).perform()

# driver.quit()