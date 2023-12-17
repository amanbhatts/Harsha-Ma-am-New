import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = None
@given('the user is on the Contact Us page')
def open_contact_us_page(context):
    global browser
    browser = webdriver.Chrome()
    browser.get("https://automationexercise.com/contact_us")

@when('they enter name "{name}", email "{email}", subject "{subject}", and message "{message}"')
def enter_contact_details(context, name, email, subject, message):
    name_field = browser.find_element(By.XPATH, "//input[@name='name']")
    email_field = browser.find_element(By.XPATH, "//input[@name='email']")
    subject_field = browser.find_element(By.XPATH, "//input[@name='subject']")
    message_field = browser.find_element(By.XPATH, "//textarea[@name='message']")

    name_field.send_keys(name)
    email_field.send_keys(email)
    subject_field.send_keys(subject)
    message_field.send_keys(message)

@when('they click on the submit button')
def click_submit_button(context):
    submit_button = browser.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    time.sleep(2)

    alert = browser.switch_to.alert
    alert.accept()

@then('a success message is displayed')
def verify_success_message(context):
    success_message = browser.find_element(By.XPATH, "//div[@class='status alert alert-success']")
    assert success_message.is_displayed()


