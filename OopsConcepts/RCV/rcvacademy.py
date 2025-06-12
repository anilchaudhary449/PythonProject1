from OopsConcepts.RCV.browser import driver,wait,EC,By,Select,time,actions,Keys

class Main_Window():
    #CheckBoxes
def checkboxes(self):
    Selenium_Java= wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Selenium with Java']")))
    Selenium_Java.click()
    print("Checkbox:", Selenium_Java.text)

    SeleniumPython= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Python']")))
    SeleniumPython.click()
    print("Checkbox:",SeleniumPython.text)

#Radio buttons
def radio_buttons(self):
    Css= wait.until(EC.element_to_be_clickable((By.ID, "css")))
    Css.click()
    print("Radio Button: Css")
    Python_opt=wait.until(EC.element_to_be_clickable((By.ID, "python")))
    Python_opt.click()
    print("Radio Button: Python_opt")

#Dropdowns
def drop_downs(self):
    DropDown=Select(driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]"))
    time.sleep(2)
    DropDown.select_by_visible_text("Meta")
    DropDown.select_by_index(2)
    DropDown.select_by_value("rcvacademy")

#Js-Popup Alert Boxes
def alert_popups(self):
    AlertBox= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[1]")))
    driver.execute_script("arguments[0].click()",AlertBox)
    alert1=driver.switch_to.alert
    print(alert1.text)
    alert1.accept()

def prompt_box_popups(self):
    PromptBox= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[2]")))
    PromptBox.click()
    alert2=driver.switch_to.alert
    print(alert2.text)
    alert2.accept()

def confirmation_popup(self):
    ConfirmationAlert= wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@value='Click me'])[3]")))
    driver.execute_script("arguments[0].click()",ConfirmationAlert)
    alert3=driver.switch_to.alert
    print(alert3.text)
    alert3.accept()


#open new browser window
def new_browser_window(self):
    BrowseNewWindow= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@onclick='myFunctionNewBrowser()']")))
    driver.execute_script("arguments[0].click()",BrowseNewWindow)
    print(BrowseNewWindow.text)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def new_tab(self):
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
def hover_element(self):
    mouseHover= wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class='dropbtn']")))
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",mouseHover)

    actions.move_to_element(mouseHover).perform()
    mouseHover.send_keys(Keys.TAB)
    time.sleep(2)
    actions.send_keys(Keys.ENTER).release().perform()
    print("MouseOver: ",mouseHover.text)
    time.sleep(4)

def tags(self):
    Tags= wait.until(EC.presence_of_element_located((By.ID,"tags")))
    Tags.send_keys("A")
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).release().perform()

def drag_me(self):
    drag_me_opt=wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@data-uniqid='1696675101602']")))
    drag_here=wait.until(EC.presence_of_element_located((By.ID,"droppable")))
    driver.execute_script("arguments[0].scrollIntoView(true)", drag_me_opt)
    actions.drag_and_drop(drag_me_opt, drag_here).release().perform()
    print(drag_here.text)

def selectable(self):
    Item4_selectable=wait.until(EC.presence_of_element_located((By.XPATH,"//li[text()='Item 4']")))
    Item4_selectable.click()
    print(Item4_selectable.text)
    Item5_selectable=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()='Item 5']")))
    Item5_selectable.click()
    print(Item5_selectable.text)

def tool_tip(self):
    Tooltip= wait.until(EC.presence_of_element_located((By.ID,"age")))
    actions.move_to_element(Tooltip).perform()
    Tooltip.send_keys("23")

def show_hide(Show_hide_btn):
    Show_hide_btn= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='myFunctionshowhide()']")))
    Show_hide_btn.click()
    print("Show/Hide: ", Show_hide_btn.text)

def sliders(self):
    slider= wait.until(EC.presence_of_element_located((By.ID,"slider")))
    actions.click_and_hold(slider).move_by_offset(0,40).release().perform()

# class iFrame():
def scroll_to_iframe(self):
    time.sleep(2)
    iFrame=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='iFrame Example']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",iFrame)
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='RCV Academy eLearning Portal']"))
def nav_automation(self):
    iframe_AutomationPage=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='AUTOMATION PRACTICE PAGE']")))
    iframe_AutomationPage.click()

    #CheckBoxes
def check_box(self):
    SeleniumJava= wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Selenium with Java']")))
    SeleniumJava.click()
    print("Checkbox:",SeleniumJava.text)

    #Radio buttons
def radio_btn(self):
    CSS= wait.until(EC.element_to_be_clickable((By.ID,"css")))
    CSS.click()
    print("Radio Button: CSS")
    Python=wait.until(EC.element_to_be_clickable((By.ID,"python")))
    Python.click()
    print("Radio Button: Python")

def show_hide_btn(self):
    ScrollToShow= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Show / Hide example']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",ScrollToShow)
    Show_hide= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@onclick='myFunctionshowhide()']")))
    driver.execute_script("arguments[0].click()",Show_hide)
    print("Show/Hide: ",Show_hide.text)