import time
from traceback import format_tb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v135.input_ import dispatch_drag_event
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # Set up Firefox options
# firefox_options = Options()
# firefox_options.add_argument('--headless')
#
# # Initialize the WebDriver
# driver = webdriver.Firefox(options=firefox_options)


driver=webdriver.Firefox()
driver.maximize_window()
# Perform actions
driver.get("https://omayo.blogspot.com/")
wait= WebDriverWait(driver,10)
actions=ActionChains(driver)

def test_title():
    print(driver.title)
def test_multiselect():
    multi_select=Select(wait.until(EC.presence_of_element_located((By.ID,"multiselect1"))))
    multi_select.select_by_value("volvox")
    multi_select.select_by_visible_text("Audi")
def test_dropdown():
    old_newspaper=Select(wait.until(EC.presence_of_element_located((By.ID,"drop1"))))
    old_newspaper.select_by_value("mno")
    old_newspaper.select_by_index(1)
def test_links():
    link1=wait.until(EC.presence_of_element_located((By.ID,"link1")))
    driver.execute_script("arguments[0].scrollIntoView(true)",link1)
    link1.click()
    driver.back()
    time.sleep(5)
    link2=wait.until(EC.presence_of_element_located((By.ID,"link2")))
    driver.execute_script("arguments[0].scrollIntoView(true)",link2)
    link2.click()
    driver.back()
def test_preloaded_text():
    text= wait.until(EC.presence_of_element_located((By.ID,"textbox1")))
    driver.execute_script("arguments[0].scrollIntoView(true)",text)
    actions.click(text).key_down(Keys.CONTROL).send_keys("A").send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
    text.send_keys("Namaste, Selenium")
def test_open_window():
    newWindow= wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='SeleniumTutorial']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",newWindow)
    newWindow.click()
    driver.switch_to.window(driver.window_handles[0])
def test_button2():
    enabled_button=wait.until(EC.element_to_be_clickable((By.ID,"but2")))
    driver.execute_script("arguments[0].click()",enabled_button)
def test_button1():
    button = driver.find_element(By.ID, "but1")
    assert not button.is_enabled(), "Button should be disabled, but it is enabled."
def test_disabled_text_box():
    disabled_text_box=driver.find_element(By.ID,"tb2")
    assert not disabled_text_box.is_enabled(),"Text bos should be diable, but it is enabled."
def test_button_submit():
    submit= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",submit)
    submit.click()
def test_button_login():
    login= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Login']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",login)
    login.click()
def test_button_register():
    register= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true)", register)
    register.click()
def test_ordered_list():
    order_list= wait.until(EC.presence_of_element_located((By.ID,"HTML25")))
    list_items= order_list.find_elements(By.TAG_NAME,"li")
    for number in list_items:
        print(number.text)
def test_unordered_list():
    unorder_list=driver.find_element(By.ID,"HTML26")
    Items_list=unorder_list.find_elements(By.TAG_NAME,"li")
    for numbers in Items_list:
        print(numbers.text)
def test_display_for_time_and_disappear():
    clickBtn= wait.until(EC.element_to_be_clickable((By.ID,"alert2")))
    driver.execute_script("arguments[0].scrollIntoView(true)",clickBtn)
    clickBtn.click()
    alert=driver.switch_to.alert
    alert.accept()
def test_popup_window():
    pop_window= wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Open a popup window']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",pop_window)
    actions.click(pop_window).perform()
    driver.switch_to.window(driver.window_handles[0])
def test_upload_file():
    file_upload= wait.until(EC.element_to_be_clickable((By.ID,"uploadfile")))
    driver.execute_script("arguments[0].scrollIntoView(true)",file_upload)
    file_upload.send_keys("E:\\QA Important\\Explicit.png")
def test_timer_button():
    timerBtn= wait.until(EC.element_to_be_clickable((By.ID,"timerButton")))
    driver.execute_script("arguments[0].click()",timerBtn)
def test_disabledBtn():
    tryIt=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Try it']")))
    driver.execute_script("arguments[0].click()",tryIt)
    time.sleep(4)
    myBtn=driver.find_element(By.ID,"myBtn")
    assert not myBtn.is_enabled(),f'myBtn is Enabled.'
def test_double_click():
    double_click=driver.find_element(By.XPATH,"//button[text()=' Double click Here   ']")
    driver.execute_script("arguments[0].scrollIntoView(true)",double_click)
    actions.double_click(double_click).perform()
    driver.switch_to.alert.accept()
def test_check_this():
    checkThis= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Check this']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",checkThis)
    actions.click(checkThis).perform()
    time.sleep(11)
    opt= wait.until(EC.element_to_be_clickable((By.ID,"dte")))
    opt.click()

def test_dateHeader():
    head= driver.find_element(By.XPATH,"//h2[@class='date-header']")
    print(head.text)
def test_pageOne():
    pageOn= driver.find_element(By.CLASS_NAME,"post-outer")
    print(pageOn.text)
    page_on= wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Page One")))
    driver.execute_script("arguments[0].click()",page_on)
    time.sleep(2)
    driver.back()
def test_home():
    homeBtn= wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Home")))
    homeBtn.click()
    time.sleep(2)
    driver.back()
def test_subscribePost():
    subscribePost= wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@type='application/atom+xml']")))
    driver.execute_script("arguments[0].click()",subscribePost)
def test_textArea():
    textArea= wait.until(EC.presence_of_element_located((By.ID,"ta1")))
    actions.click(textArea.send_keys("This is text area.")).perform()
def test_textAreaTwo():
    textarea2=wait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@cols='30']")))
    driver.execute_script("arguments[0].scrollIntoView(true)",textarea2)
    actions.click(textarea2).key_down(Keys.CONTROL).send_keys("A",Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
    textarea2.send_keys("This second text area.")
def test_table():
    table=wait.until(EC.presence_of_element_located((By.ID,"table1")))
    print(table.text)
    head_table=wait.until(EC.presence_of_element_located((By.TAG_NAME, "thead")))
    print(head_table.text)
    body_table= wait.until(EC.presence_of_element_located((By.TAG_NAME,"tbody")))
    tr_table=body_table.find_elements(By.TAG_NAME,"tr")
    for tableRow in tr_table:
        print(tableRow.text)
def test_htmlForm():
    HTMLForm= wait.until(EC.presence_of_element_located((By.ID,"HTML31")))
    driver.execute_script("arguments[0].scrollIntoView(true)",HTMLForm)
    username= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']")))
    password= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='password']")))
    login= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@value='LogIn']")))
    actions.click(username.send_keys("username")).click(password.send_keys("password")).click(login).perform()
def test_frame1():
    Scroll_frame= wait.until(EC.presence_of_element_located((By.ID,"HTML21")))
    driver.execute_script("arguments[0].scrollIntoView(true)",Scroll_frame)
    driver.switch_to.frame(driver.find_element(By.ID,"iframe1"))

    blogStat= wait.until(EC.presence_of_element_located((By.ID,"HTML11")))
    driver.execute_script("arguments[0].scrollIntoView(true)", blogStat)
    print(blogStat.text)
    driver.switch_to.default_content()
def test_frame2():
    driver.switch_to.frame(driver.find_element(By.ID,"iframe2"))
    contact_meBtn= wait.until(EC.element_to_be_clickable((By.LINK_TEXT,">> Contact Me")))
    driver.execute_script("arguments[0].scrollIntoView(true)",contact_meBtn)
    contact_meBtn.click()

    footer= wait.until(EC.presence_of_element_located((By.ID,"Attribution1")))
    driver.execute_script("arguments[0].scrollIntoView(true)",footer)
    print(footer.text)
    driver.switch_to.default_content()
def test_loginPage():
    loginPage= wait.until(EC.presence_of_element_located((By.ID,"HTML42")))
    driver.execute_script("arguments[0].scrollIntoView(true)",loginPage)
    user_name= driver.find_element(By.NAME,"userid")
    pass_word= driver.find_element(By.NAME,"pswrd")
    loginBtn= driver.find_element(By.XPATH,"//input[@value='Login']")
    cancelBtn= driver.find_element(By.XPATH,"//input[@value='Cancel']")
    actions.click(user_name.send_keys("username")).click(pass_word.send_keys("password")).click(cancelBtn).perform()
    time.sleep(3)
    actions.click(user_name.send_keys("username")).click(pass_word.send_keys("password")).click(loginBtn).perform()
    msg=driver.switch_to.alert
    print(msg.text)
    msg.accept()