import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Firefox()
driver.maximize_window()

driver.get('https://authorized-partner.netlify.app/register/')

action=ActionChains(driver)
driver.implicitly_wait(5)

policyBtn= driver.find_element(By.XPATH,"//button[@id='remember']")
driver.execute_script("arguments[0].click()",policyBtn)

ContinueBtn= driver.find_element(By.XPATH,"//button[text()='Continue']")
driver.execute_script("arguments[0].click()",ContinueBtn)

#firstName
firstName= driver.find_element(By.XPATH,"//input[contains(@placeholder,'Enter Your First Name')]")
action.click(firstName).send_keys("Test1").send_keys(Keys.TAB).perform()

#lastName
action.send_keys("Test2").send_keys(Keys.TAB).perform()

#emailAddress
action.send_keys("test@gmail.com").send_keys(Keys.TAB).perform()

#phoneNumber
action.send_keys("9800009567").send_keys(Keys.TAB).send_keys(Keys.TAB).perform()

time.sleep(5)
#password
action.send_keys("Qwerttty123@").key_down(Keys.CONTROL).send_keys("A").send_keys("C").key_up(Keys.CONTROL).send_keys(Keys.TAB).perform()

time.sleep(4)
#confPassword
action.send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).send_keys(Keys.TAB).perform()

#Next
action.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

