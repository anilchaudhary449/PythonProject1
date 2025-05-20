from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox()
driver.get("https://demoqa.com/")
driver.maximize_window()

driver.implicitly_wait(5)

WidgetBtn = driver.find_element(By.XPATH, "//h5[text()='Widgets']")
driver.execute_script("arguments[0].scrollIntoView(true);", WidgetBtn)
WidgetBtn.click()

SelectMenu = driver.find_element(By.XPATH, "//span[text()='Select Menu']")
driver.execute_script("arguments[0].scrollIntoView(true);", SelectMenu)
SelectMenu.click()

select_value_dropdown =driver.find_element(By.XPATH, "//div[contains(@id,'withOptGroup')]")
select_value_dropdown.click()
value_option=driver.find_element(By.XPATH,"//div[text()='Group 1, option 2']")
value_option.click()

select_one_dropdown= driver.find_element(By.ID,"selectOne")
select_one_dropdown.click()
select_title= driver.find_element(By.CSS_SELECTOR,"#react-select-3-input")
select_title.send_keys("Mr.",Keys.ENTER)

old_select_menu = Select(driver.find_element(By.ID, "oldSelectMenu"))
old_select_menu.select_by_visible_text("Green")

multiselect_drop= driver.find_element(By.XPATH,"//*[contains(text(),'Select...')]")
driver.execute_script("arguments[0].scrollIntoView(true)",multiselect_drop)
multiselect_drop.click()

driver.implicitly_wait(4)
multiselect_opt= driver.find_element(By.XPATH,"//input[@id='react-select-4-input']")
multiselect_opt.send_keys("Green",Keys.ENTER)
multiselect_opt.send_keys("Black",Keys.ENTER)
multiselect_opt.send_keys("Red",Keys.ENTER)
multiselect_opt.send_keys(Keys.ENTER)

multi_select_drop= Select(driver.find_element(By.ID,"cars"))
multi_select_drop.select_by_value("volvo")
multi_select_drop.select_by_visible_text("Audi")
multi_select_drop.select_by_index(2)

driver.quit()
