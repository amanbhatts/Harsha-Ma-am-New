import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = None

@given('the user is on the Sauce Demo login page')
def open_sauce_demo_login_page(context):
    global browser
    browser = webdriver.Chrome()
    browser.get("https://www.saucedemo.com/")

@when('they enter username "{username}" and password "{password}"')
def enter_login_credentials(context, username, password):
    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

@when('they click on the login button')
def click_login_button(context):
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

@then('they should be logged in successfully')
def verify_successful_login(context):
    assert "inventory.html" in browser.current_url.lower(), "Login was not successful"


