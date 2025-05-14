import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver= webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

time.sleep(3)

Username= driver.find_element(By.XPATH,"//input[@id='user-name']")
Username.send_keys('performance_glitch_user')

time.sleep(3)
Password= driver.find_element(By.XPATH,"//input[@id='password']")
Password.send_keys('secret_sauce')

time.sleep(4)
login_btn=driver.find_element(By.XPATH,"//input[@id='login-button']")
login_btn.click()


time.sleep(4)
Filter= driver.find_element(By.XPATH,"//option[text()='Price (low to high)']")
Filter.click()

time.sleep(6)
#add_to_cart Based on //tag_name
Backpack= driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
Backpack.click()

#using //text
# Backpack= driver.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']")
# Backpack.click()
time.sleep(3)
BoltTShirt= driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
BoltTShirt.click()
time.sleep(3)
FleeceJacket= driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
FleeceJacket.click()

time.sleep(5)
Cart= driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']")
Cart.click()

time.sleep(5)
#removeFromCart
Remove_Backpack= driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']")
Remove_Backpack.click()

time.sleep(5)
Checkout= driver.find_element(By.XPATH,"//button[@id='checkout']")
Checkout.click()

time.sleep(5)
F_name= driver.find_element(By.XPATH,"//input[@id='first-name']")
F_name.send_keys("Tester1")

time.sleep(3)
L_name= driver.find_element(By.XPATH,"//input[@id='last-name']")
L_name.send_keys(" TESTER1")

time.sleep(5)
Postal_code= driver.find_element(By.XPATH,"//input[@id='postal-code']")
Postal_code.send_keys("12345")

time.sleep(5)
Continue= driver.find_element(By.XPATH,"//input[@id='continue']")
Continue.click()

time.sleep(5)
Finish= driver.find_element(By.XPATH,"//button[@id='finish']")
Finish.click()

time.sleep(5)
Back_to_Home= driver.find_element(By.XPATH,"//button[@id='back-to-products']")
Back_to_Home.click()

time.sleep(7)

driver.quit()