import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()



Elements= driver.find_element(By.XPATH,"//h5[text()='Elements']")
driver.execute_script("arguments[0].click()",Elements)

time.sleep(5)
Button_btn= driver.find_element(By.XPATH,"(//span[contains(@class,'text')])[5]")
Button_btn.click()

time.sleep(5)
Click_Me= driver.find_element(By.XPATH,"//button[text()='Click Me']")
driver.execute_script("arguments[0].click()",Click_Me)


time.sleep(5)
# #mouseAction
# action=ActionChains(driver)
