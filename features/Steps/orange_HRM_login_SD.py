from datetime import time

from behave import *

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open the HRM page')
def open_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(4)


@when('enter username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys(password)


@when('click on login button')
def click_login(context):
    context.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()


@then('user must successfully login to dashboard')
def dashboard(context):
    context.driver.find_element(By.XPATH, "//header/div[1]/div[1]").is_displayed()
