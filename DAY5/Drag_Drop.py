import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://demoqa.com")
driver.maximize_window()
action=ActionChains(driver)

Interaction= driver.find_element(By.XPATH,"//h5[text()='Interactions']")
driver.execute_script("arguments[0].click()",Interaction)

Droppable= driver.find_element(By.XPATH,"//span[text()='Droppable']")
driver.execute_script("arguments[0].click()",Droppable)

time.sleep(3)
Simple_dragMe= driver.find_element(By.ID,"draggable")
Simple_DropHere= driver.find_element(By.ID,"droppable")
action.drag_and_drop(Simple_dragMe,Simple_DropHere).perform()

time.sleep(3)
Accept_tab= driver.find_element(By.ID,"droppableExample-tab-accept")
Accept_tab.click()

time.sleep(3)
Accept_NotAcceptable= driver.find_element(By.ID,"notAcceptable")
Accept_DropHere2= driver.find_element(By.XPATH,"(//div[@id='droppable'])[2]")
action.drag_and_drop(Accept_NotAcceptable,Accept_DropHere2).perform()

time.sleep(3)
Accept_Acceptable= driver.find_element(By.ID,"acceptable")
Accept_DropHere1= driver.find_element(By.XPATH,"(//div[@id='droppable'])[2]")
action.drag_and_drop(Accept_Acceptable,Accept_DropHere1).perform()

time.sleep(3)
Prevent_Propogation= driver.find_element(By.ID,"droppableExample-tab-preventPropogation")
Prevent_Propogation.click()

time.sleep(2)
Drag_Me_btn1= driver.find_element(By.XPATH,"//div[text()='Drag Me']")
notGreedyOuter_droppable1= driver.find_element(By.XPATH,"(//p[text()='Outer droppable'])[1]")
action.drag_and_drop(Drag_Me_btn1,notGreedyOuter_droppable1).release().perform()

time.sleep(3)
notGreedy_innerDroppable=driver.find_element(By.ID,"notGreedyInnerDropBox")
action.drag_and_drop(Drag_Me_btn1,notGreedy_innerDroppable).release().perform()

time.sleep(2)
Drag_Me_btn2= driver.find_element(By.XPATH,"//div[text()='Drag Me']")
greedyOuter_droppable2= driver.find_element(By.XPATH,"//div[@id='greedyDropBox']")
driver.execute_script("arguments[0].scrollIntoView(true);",greedyOuter_droppable2)
action.drag_and_drop(Drag_Me_btn2,greedyOuter_droppable2).release().perform()

time.sleep(3)
Greedy_innerDroppable=driver.find_element(By.XPATH,"//div[@id='greedyDropBoxInner']")
action.drag_and_drop(Drag_Me_btn2,Greedy_innerDroppable).release().perform()

time.sleep(3)
Revert_draggable= driver.find_element(By.ID,"droppableExample-tab-revertable")
driver.execute_script("arguments[0].scrollIntoView(true);",Revert_draggable)
driver.execute_script("arguments[0].click()",Revert_draggable)

time.sleep(3)
Will_Revert= driver.find_element(By.ID,"revertable")
WillNotRevert= driver.find_element(By.ID,"notRevertable")
DropBox= driver.find_element(By.XPATH,"(//div[@id='droppable'])[3]")


action.drag_and_drop(Will_Revert,DropBox).perform()
time.sleep(3)
action.drag_and_drop(WillNotRevert,DropBox).perform()

driver.quit()