import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()
action= ActionChains(driver)

Interaction= driver.find_element(By.XPATH,"//h5[text()='Interactions']")
driver.execute_script("arguments[0].click()",Interaction)

Dragabble= driver.find_element(By.XPATH,"//span[text()='Dragabble']")
driver.execute_script("arguments[0].click()",Dragabble)

Drag_ME= driver.find_element(By.XPATH,"//div[text()='Drag me']")
action.click_and_hold(Drag_ME).move_by_offset(200,50).release().perform()

time.sleep(2)
AxisRestricted= driver.find_element(By.XPATH,"//a[text()='Axis Restricted']")
AxisRestricted.click()

time.sleep(3)
Only_X= driver.find_element(By.XPATH,"//div[text()='Only X']")
action.click_and_hold(Only_X).move_by_offset(100,0).release().perform()

time.sleep(5)
Only_Y= driver.find_element(By.XPATH,"//div[text()='Only Y']")
action.click_and_hold(Only_Y).move_by_offset(0,100).release().perform()

time.sleep(3)
ContainerRestricted_btn=driver.find_element(By.XPATH,"//a[text()='Container Restricted']")
ContainerRestricted_btn.click()

Container_Restricted1= driver.find_element(By.XPATH,"//div[contains(@class,'draggable ui-widget-content ui-draggable ui-draggable-handle') ]")
action.click_and_hold(Container_Restricted1).move_by_offset(100,50).release().perform()

time.sleep(3)
Container_Restricted2=driver.find_element(By.XPATH,"//span[contains(@class,'ui-widget-header ui-draggable ui-draggable-handle')]")
action.click_and_hold(Container_Restricted2).move_by_offset(100,50).release().perform()

Cursor_Style= driver.find_element(By.XPATH,"//a[text()='Cursor Style']")
Cursor_Style.click()

CursorCenter= driver.find_element(By.ID,"cursorCenter")
action.click_and_hold(CursorCenter).move_by_offset(100,50).release().perform()

time.sleep(3)
CursorLeft= driver.find_element(By.ID,"cursorTopLeft")
action.click_and_hold(CursorLeft).move_by_offset(100,50).release().perform()

time.sleep(3)
CursorBottom= driver.find_element(By.ID,"cursorBottom")
action.click_and_hold(CursorBottom).move_by_offset(100,50).release().perform()

# source= driver.find_element(By.ID,"")
# target= driver.find_element(By.ID,"")
# action.drag_and_drops(source,target)