import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios('../features\login.feature')

@pytest.fixture
def driver():
    browser= webdriver.Firefox()
    yield browser
    browser.quit()

@given('the user is on the login page')
def navigate_to_login(driver):
    driver.get("https://sanitize-crm.netlify.app/")

time.sleep(3)
@when('the user enters valid credentials')
def enter_credentials(driver):
    #username
    uname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    uname.send_keys("anil.bhumal@gmail.com")
    #password
    password=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))
    )
    password.send_keys("P@$$w0rd$")
    #login button
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
@then('the user should be logged in')
def verify_login(driver):
    assert driver.title=="Sanitize Email"