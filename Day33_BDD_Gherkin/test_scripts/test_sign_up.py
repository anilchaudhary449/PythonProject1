import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios('../features\signup.feature')
@pytest.fixture
def driver():
    browser= webdriver.Firefox()
    yield browser
    browser.quit()

@given('the user is on the sign up page')
def navigate_to_signup(driver):
    driver.get("https://sanitize-crm.netlify.app/sign-up")
@when('the user register with valid datas')
def enter_valid_datas(driver):
    #name
    name= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))
    name.send_keys("Test1")
    #email
    email=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"email")))
    email.send_keys("email@gmail.com")
    #password
    password=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"password")))
    password.send_keys("Password")
    #policyBtn
    policyBtn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@role='checkbox']")))
    policyBtn.click()
    #submit
    signup= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    signup.click()
@then('the user should be redirected to login page')
def verify_page(driver):
    assert "Sanitize Email"==driver.title