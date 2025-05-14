from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the driver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)  #10-Seconds timeout

#try:
#Navigate to the website
driver.get("https://demoqa.com")
driver.maximize_window()

# Wait for and click on 'Elements'
elements_section = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.card:nth-child(1)")))
driver.execute_script("arguments[0].scrollIntoView(true);", elements_section)
elements_section.click()

# Wait for and click on Elements accordion
elements_accordion = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "group-header")))
driver.execute_script("arguments[0].scrollIntoView(true);", elements_accordion)
ActionChains(driver).move_to_element(elements_accordion).click().perform()

# Wait for and click on Text Box
text_box = wait.until(EC.element_to_be_clickable((By.ID, "item-0")))
text_box.click()

# Fill in the form
wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("Anil Chaudhary")
wait.until(EC.presence_of_element_located((By.ID, "userEmail"))).send_keys("abc@gmail.com")
wait.until(EC.presence_of_element_located((By.ID, "currentAddress"))).send_keys("Test Current Address")
wait.until(EC.presence_of_element_located((By.ID, "permanentAddress"))).send_keys("Test Permanent Address")

# Submit the form
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

# finally:
# Close the browser
# driver.quit()  # Using quit() instead of close() to ensure all browser instances are closed