from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://demoqa.com")
driver.maximize_window()
wait=WebDriverWait(driver,15)

Form= wait.until(EC.presence_of_element_located((By.XPATH,"//h5[text()='Forms']")))
driver.execute_script("arguments[0].click()",Form)

PracticeForm= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Practice Form']")))
driver.execute_script("arguments[0].click()",PracticeForm)

firstName= wait.until(EC.presence_of_element_located((By.ID,"firstName")))
firstName.send_keys("Test")

lastName= wait.until(EC.presence_of_element_located((By.ID,"lastName")))
lastName.send_keys("Tester")

Email= wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
Email.send_keys("email@gmail.com")

Gender= wait.until(EC.presence_of_element_located((By.ID,"gender-radio-1")))
driver.execute_script("arguments[0].click()",Gender)

MobileNumber= wait.until(EC.presence_of_element_located((By.ID,"userNumber")))
MobileNumber.send_keys("9876543201")

DoB= wait.until(EC.presence_of_element_located((By.ID,"dateOfBirthInput")))
driver.execute_script("arguments[0].click()",DoB)

dateClick= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='20']")))
dateClick.click()

Subjects= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#subjectsInput")))
driver.execute_script("arguments[0].scrollIntoView(true)",Subjects)
Subjects.send_keys("M")
SubjectOpt= wait.until(EC.presence_of_element_located((By.XPATH,"//div[text()='Commerce']")))
SubjectOpt.click()

Hobbies= wait.until(EC.presence_of_element_located((By.ID,"hobbies-checkbox-1")))
driver.execute_script("arguments[0].click()",Hobbies)

Picture= wait.until(EC.element_to_be_clickable((By.ID,"uploadPicture")))
Picture.send_keys("E:\\QA Important\\Explicit.png")

CurAddress= wait.until(EC.presence_of_element_located((By.ID,"currentAddress")))
CurAddress.send_keys("ABC")

SelectState=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'css-1wa3eu0-placeholder') and contains(text(), 'Select State')]")))
SelectState.click()

StateOpt= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Rajasthan']")))
driver.execute_script("arguments[0].click()",StateOpt)


StateCity= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Select City']")))
StateCity.click()

CityOpt=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Jaipur']")))
CityOpt.click()

SubmitBtn= wait.until(EC.element_to_be_clickable((By.ID,"submit")))
SubmitBtn.click()

CloseBtn=wait.until(EC.element_to_be_clickable((By.ID,'closeLargeModal')))
driver.execute_script("arguments[0].click()",CloseBtn)

driver.quit()






