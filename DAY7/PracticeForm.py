import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Firefox()
driver.get("https://demoqa.com")
driver.maximize_window()


actions=ActionChains(driver)

Form= driver.find_element(By.XPATH,"//h5[text()='Forms']")
driver.execute_script("arguments[0].click()",Form)

PracticeForm= driver.find_element(By.XPATH,"//span[text()='Practice Form']")
driver.execute_script("arguments[0].click()",PracticeForm)

firstName= driver.find_element(By.ID,"firstName")
actions.click(firstName).send_keys("Anila"+Keys.ENTER).perform()

lastName= driver.find_element(By.ID,"lastName")
actions.click(lastName).send_keys("Chaudhary"+Keys.ENTER).perform()

time.sleep(3)
Email= driver.find_element(By.ID,"userEmail")
actions.click(Email).key_down(Keys.ENTER).send_keys("email@gmail.com").key_up(Keys.ENTER).perform()

time.sleep(3)
Gender= driver.find_element(By.XPATH,"//*[text()='Gender']")
actions.click(Gender).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
time.sleep(3)
MobileNumber= driver.find_element(By.ID,"userNumber")
actions.click(MobileNumber).send_keys("9876543201").perform()

# time.sleep(3)
# DoB= driver.find_element(By.XPATH,"//*[contains(@id,'dateOfBirthInput')]")
# actions.click(DoB).send_keys(Keys.ENTER).send_keys(Keys.ARROW_DOWN).perform()

Subjects= driver.find_element(By.CSS_SELECTOR,"#subjectsInput")
driver.execute_script("arguments[0].scrollIntoView(true)",Subjects)
actions.click(Subjects.send_keys("Maths")).perform()







