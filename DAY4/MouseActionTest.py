from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()
action= ActionChains(driver)

Elements= driver.find_element(By.XPATH,"//h5[text()='Elements']")
driver.execute_script("arguments[0].click()",Elements)

Button_btn= driver.find_element(By.XPATH,"(//span[contains(@class,'text')])[5]")
Button_btn.click()

Click_Me= driver.find_element(By.XPATH,"//button[text()='Click Me']")
driver.execute_script("arguments[0].click()",Click_Me)

Double_Click_Me= driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
action.double_click(Double_Click_Me).perform()

Right_Click_me= driver.find_element(By.XPATH,"//button[text()='Right Click Me']")
action.context_click(Right_Click_me).perform()