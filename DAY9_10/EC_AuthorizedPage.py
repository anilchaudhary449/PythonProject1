from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://authorized-partner.netlify.app/login")
wait=WebDriverWait(driver,10)

UEmail=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
UEmail.send_keys("cefavo7705@dlbazi.com")
Password=wait.until(EC.presence_of_element_located((By.ID,"password")))
Password.send_keys("Admin@123")

LoginBtn= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@type,'submit')]")))
driver.execute_script("arguments[0].click()",LoginBtn)

AddApplication=wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Add New Application']")))
driver.execute_script("arguments[0].click()",AddApplication)

fullName= wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@placeholder,'Enter Your Full Name')]")))
fullName.send_keys("Test Tester")

calender= wait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(@class,'lucide lucide-calendar1 mr-2 size-4')]")))
calender.click()
dateClick= wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='29']")))
dateClick.click()
Done=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Done']")))
Done.click()

email=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='email']")))
email.send_keys("tester@test.com")

phone=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='phoneNumber']")))
phone.send_keys("9865643243")

NextBtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button'][.//text()='Next']")))
NextBtn.click()

SelectCountry=wait.until(EC.presence_of_element_located((By.XPATH,"//label[text()='Preferred Country']")))
SelectCountry.click()

SelectOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='New Zealand']")))
driver.execute_script("arguments[0].click()",SelectOpt)

DegreeType= wait.until(EC.presence_of_element_located((By.XPATH,"//label[text()='Degree Type']")))
DegreeType.click()

DegreeOpt= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Masters']")))
driver.execute_script("arguments[0].click()",DegreeOpt)

University= wait.until(EC.presence_of_element_located((By.XPATH,"//label[text()='University']")))
University.click()

# option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Annette']")))
# driver.execute_script("arguments[0].click()",option)

