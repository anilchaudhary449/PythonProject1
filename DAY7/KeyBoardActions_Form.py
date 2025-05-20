from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(options=options)
driver.get("https://demoqa.com")
driver.maximize_window()

actions=ActionChains(driver)

driver.implicitly_wait(10)

Form= driver.find_element(By.XPATH,"//h5[text()='Forms']")
driver.execute_script("arguments[0].click()",Form)

PracticeForm= driver.find_element(By.XPATH,"//span[text()='Practice Form']")
driver.execute_script("arguments[0].click()",PracticeForm)

# firstName= driver.find_element(By.ID,"firstName")
# firstName.click()
actions.click(driver.find_element(By.ID,"firstName")).send_keys("Tester1").send_keys(Keys.TAB).perform()

#lastname
actions.send_keys("Tester2").send_keys(Keys.TAB).perform()

#email
actions.send_keys("tester@gmail.com").send_keys(Keys.TAB).perform()

#close
actions.key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()

#gender
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.SPACE).send_keys(Keys.TAB).perform()
time.sleep(5)
#mobileNumber
actions.send_keys("9876543210").send_keys(Keys.TAB).perform()
time.sleep(5)
#DateOfBirth
actions.key_down(Keys.TAB).send_keys(Keys.ARROW_DOWN).key_up(Keys.TAB).send_keys(Keys.ENTER).perform()

time.sleep(5)
#subjects
SubjectBtn= driver.find_element(By.XPATH,"//*[@class='subjects-auto-complete__control css-yk16xz-control']")
driver.execute_script("arguments[0].click()",SubjectBtn)
actions.click(SubjectBtn).send_keys("Maths").perform()

time.sleep(5)
driver.execute_script("window.scrollBy(0, 500);")
#hobbies
actions.send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.SPACE).send_keys(Keys.TAB).send_keys(Keys.SPACE).perform()

time.sleep(5)
#picture
upload=driver.find_element(By.ID,"uploadPicture")
upload.send_keys("C:\\Users\\anilb\\Downloads\\Screenshot 2025-05-19 223237.png")

time.sleep(5)
#address
actions.click(driver.find_element(By.ID,"currentAddress")).send_keys("abc").send_keys(Keys.TAB).perform()

time.sleep(5)
#selectState
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()

time.sleep(5)
#selectCity
actions.send_keys(Keys.TAB+Keys.ARROW_DOWN+Keys.TAB).perform()

time.sleep(5)
#submit
actions.send_keys(Keys.ENTER).perform()

time.sleep(3)
print("Form submitted using keyboard actions!")
time.sleep(4)
#Close
actions.send_keys(Keys.ESCAPE).perform()

driver.quit()