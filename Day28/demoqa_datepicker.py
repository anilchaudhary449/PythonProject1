import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://demoqa.com/")

action=ActionChains(driver)
wait= WebDriverWait(driver,10)

widget= wait.until(EC.presence_of_element_located((By.XPATH,"//h5[text()='Widgets']")))
driver.execute_script("arguments[0].click()",widget)

date_picker= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Date Picker']")))
driver.execute_script("arguments[0].click()",date_picker)

time.sleep(2)
# select_date= wait.until(EC.presence_of_element_located((By.ID,"datePickerMonthYearInput")))
# driver.execute_script("arguments[0].click()", select_date)

# select_date_opt= wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,'Choose Sunday, June 22nd, 2025')]")))
# driver.execute_script("arguments[0].click()", select_date_opt)

select_date=wait.until(EC.presence_of_element_located((By.ID,"datePickerMonthYearInput")))
action.click(select_date).key_down(Keys.CONTROL).send_keys("A").send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
select_date.send_keys("07/07/2025",Keys.ENTER)

# date_time= wait.until(EC.presence_of_element_located((By.ID,"dateAndTimePickerInput")))
# driver.execute_script("arguments[0].click()",date_time)
# time.sleep(2)
# select_Date= wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Choose Friday, June 20th, 2025']")))
# driver.execute_script("arguments[0].click()", select_Date)
#
# select_time= wait.until(EC.presence_of_element_located((By.XPATH,"//li[text()='00:15']")))
# driver.execute_script("arguments[0].click()", select_time)

select_Date=wait.until(EC.presence_of_element_located((By.ID,"dateAndTimePickerInput")))
action.click(select_Date).key_down(Keys.CONTROL).send_keys("A").send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
select_Date.send_keys("June 26, 2025 2:20 PM")
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.quit()
