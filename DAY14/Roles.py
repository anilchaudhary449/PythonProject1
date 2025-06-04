import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox()
driver.maximize_window()
driver.get("https://sanitize-crm.netlify.app/login")
wait= WebDriverWait(driver,15)

userName=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='email']")))
userName.send_keys("fitefi2554@pricegh.com")

userPass=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
userPass.send_keys("P@$$w0rd")

LoginBtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
LoginBtn.click()

time.sleep(9)
Alpha_account= wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='lucide lucide-chevron-down']")))
Alpha_account.click()

time.sleep(3)
Settings= wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Settings']")))
driver.execute_script("arguments[0].click()",Settings)

Roles= wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='Roles']")))
driver.execute_script("arguments[0].scrollIntoView(true)",Roles)
Roles.click()

CreateRole= wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()=' Create Role']")))
driver.execute_script("arguments[0].click()",CreateRole)

roleName= wait.until(EC.presence_of_element_located((By.ID,"role-name")))
roleName.send_keys("developer")

#view
Role= wait.until(EC.presence_of_element_located((By.ID, "roles-View")))
Role.click()

myTeams= wait.until(EC.presence_of_element_located((By.ID,"my_team-View")))
myTeams.click()

apikey= wait.until(EC.presence_of_element_located((By.ID,"api_key-View")))
apikey.click()

analyzeList= wait.until(EC.presence_of_element_located((By.ID,"analyze_list-View")))
analyzeList.click()

verifyEmail= wait.until(EC.presence_of_element_located((By.ID,"verify_email-View")))
verifyEmail.click()

cleanEmail= wait.until(EC.presence_of_element_located((By.ID,"clean_email-View")))
cleanEmail.click()

Edit= wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/form/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/button")))
Edit.click()

Add= wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/form/div[1]/div[2]/div[2]/div[1]/div[1]/div[4]/button")))
Add.click()

Delete= wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/form/div[1]/div[2]/div[2]/div[1]/div[1]/div[5]/button")))
Delete.click()

specialPermission= wait.until(EC.presence_of_element_located((By.ID,"my-plan-permission")))
specialPermission.click()

CreateNewRoleBtn= wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Create New Role']")))
driver.execute_script("arguments[0].click()",CreateNewRoleBtn)
