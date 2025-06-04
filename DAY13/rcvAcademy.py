import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://training.rcvacademy.com/test-automation-practice-page")

wait=WebDriverWait(driver,10)
actions=ActionChains(driver)
#CheckBoxes
SeleniumJava= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
SeleniumJava.click()
print("Checkbox:",SeleniumJava.text)

SeleniumPython= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Python']")))
SeleniumPython.click()
print("Checkbox:",SeleniumPython.text)

#Radio buttons
CSS= wait.until(EC.element_to_be_clickable((By.ID,"css")))
CSS.click()
print("Radio Button: CSS")
Python=wait.until(EC.element_to_be_clickable((By.ID,"python")))
Python.click()
print("Radio Button: Python")

#Dropdowns
DropDown=Select(driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]"))
time.sleep(2)
DropDown.select_by_visible_text("Meta")
DropDown.select_by_index(2)
DropDown.select_by_value("rcvacademy")

#Js-Popup Alert Boxes
AlertBox= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[1]")))
driver.execute_script("arguments[0].click()",AlertBox)
alert1=driver.switch_to.alert
print(alert1.text)
alert1.accept()

PromptBox= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[2]")))
PromptBox.click()
alert2=driver.switch_to.alert
print(alert2.text)
alert2.accept()

ConfirmationAlert= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[3]")))
driver.execute_script("arguments[0].click()",ConfirmationAlert)
alert3=driver.switch_to.alert
print(alert3.text)
alert3.accept()


#open new browser window
BrowseNewWindow= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@onclick='myFunctionNewBrowser()']")))
driver.execute_script("arguments[0].click()",BrowseNewWindow)
print(BrowseNewWindow.text)

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
BrowseNewTab= wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Click to visit RCV Academy!']")))
driver.execute_script("arguments[0].click()",BrowseNewTab)
print(BrowseNewTab.text)

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(1)

#hover over element
mouseHover= wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class='dropbtn']")))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",mouseHover)

actions.move_to_element(mouseHover).perform()
mouseHover.send_keys(Keys.TAB)
time.sleep(2)
actions.send_keys(Keys.ENTER).release().perform()
print("MouseOver: ",mouseHover.text)
time.sleep(4)

Tags= wait.until(EC.presence_of_element_located((By.ID,"tags")))
Tags.send_keys("A")
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).release().perform()

drag_me=wait.until(EC.element_to_be_clickable((By.XPATH,"//p[@data-uniqid='1696675101602']")))
drag_here=wait.until(EC.presence_of_element_located((By.ID,"droppable")))
driver.execute_script("arguments[0].scrollIntoView(true)",drag_me)
actions.drag_and_drop(drag_me,drag_here).release().perform()
print(drag_here.text)

Item4_selectable=wait.until(EC.presence_of_element_located((By.XPATH,"//li[text()='Item 4']")))
Item4_selectable.click()
print(Item4_selectable.text)
Item5_selectable=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()='Item 5']")))
Item5_selectable.click()
print(Item5_selectable.text)

Tooltip= wait.until(EC.presence_of_element_located((By.ID,"age")))
actions.move_to_element(Tooltip).perform()
Tooltip.send_keys("23")

Show_hide= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@onclick='myFunctionshowhide()']")))
Show_hide.click()
print("Show/Hide: ",Show_hide.text)

slider= wait.until(EC.presence_of_element_located((By.ID,"slider")))
actions.click_and_hold(slider).move_by_offset(0,40).release().perform()

time.sleep(2)
iFrame=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='iFrame Example']")))
driver.execute_script("arguments[0].scrollIntoView(true)",iFrame)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='RCV Academy eLearning Portal']"))
iframe_AutomationPage=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='AUTOMATION PRACTICE PAGE']")))
iframe_AutomationPage.click()

#CheckBoxes
SeleniumJava= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
SeleniumJava.click()
print("Checkbox:",SeleniumJava.text)

#Radio buttons
CSS= wait.until(EC.element_to_be_clickable((By.ID,"css")))
CSS.click()
print("Radio Button: CSS")
Python=wait.until(EC.element_to_be_clickable((By.ID,"python")))
Python.click()
print("Radio Button: Python")

ScrollToShow= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Show / Hide example']")))
driver.execute_script("arguments[0].scrollIntoView(true)",ScrollToShow)
Show_hide= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@onclick='myFunctionshowhide()']")))
driver.execute_script("arguments[0].click()",Show_hide)
print("Show/Hide: ",Show_hide.text)

driver.switch_to.default_content()

# driver.quit()