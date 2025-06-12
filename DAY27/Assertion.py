import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://sanitize-crm.netlify.app/")

# expected_url = "https://sanitize-crm.netlify.app/login"
# actual_url = driver.current_url
# assert actual_url == expected_url, f"Expected URL '{expected_url}' but got '{actual_url}'"

wait=WebDriverWait(driver,10)

email= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))
email.send_keys("anil.bhumal@gmail.com")
password= wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
password.send_keys("P@$$w0rd")

login=wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
login.click()


# expected_title="Sanitize Email"
# actual_title=driver.title
# assert actual_title==expected_title, f" Your Expected Title '{expected_title} but Actual Title '{actual_title}'"


# element=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@role='alert']")))
# print("Alert: ",element.text)
# assert "Login successful" in element.text

# element=wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Welcome,']")))
#
# assert "Welcome," in element.text
# print("Element: ",element.text)

# element= driver.find_element(By.TAG_NAME,"z")
# assert element.is_displayed(),f"z is invisible"

# element=wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Welcome,']")))
# expected_text = "Welcome"
# actual_text = element.text
# assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"

# button= driver.find_element(By.TAG_NAME,"button")
# print(button.tag_name)
# print(button.get_attribute('outerHTML'))
# assert button.is_enabled(),f"Button isn't enabled."
button = driver.find_element(By.TAG_NAME, "button")
assert button.is_enabled(), "Button isn't enabled."


driver.quit()