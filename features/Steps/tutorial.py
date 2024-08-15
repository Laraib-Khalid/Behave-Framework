# from behave import *
#
# @given('Open google')
# def step_impl("https://www.google.com"):
#     pass
#
# @when('we implement a test')
# def step_impl(context):
#     assert True is not False
#
# @then('behave will test it for us!')
# def step_impl(context):
#     assert context.failed is False
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Search = "Robot Framework"

@given('the browser is open')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Or whichever driver you are using
    context.driver.maximize_window()

@when('I navigate to Google')
def step_impl(context):
    context.driver.get("https://www.google.com")

@then('the Google homepage should be displayed')
def step_impl(context):
    time.sleep(2)  # Let the user actually see something!
    assert "Google" in context.driver.title
    # context.driver.quit()

@when('I search for search query')
def step_impl(context):
    loc = context.driver.find_element(By.ID,"APjFqb")
    loc.send_keys(Search + Keys.RETURN)


@then('I should see search results for search query')
def step_impl(context):
    # time.sleep(2)  # Wait for the search results to load
    assert Search in context.driver.title, f"Expected '{Search}' in title, but found '{context.driver.title}'"
    assert len(context.driver.find_elements(By.CSS_SELECTOR, "div.g")) > 0, "No search results found"
    context.driver.quit()

