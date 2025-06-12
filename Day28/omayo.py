import time

from selenium import webdriver
from selenium.webdriver.common.by import By
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

