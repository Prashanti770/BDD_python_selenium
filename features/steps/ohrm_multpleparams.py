import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)

@when('I Open OrangeHrm page')
def openurl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('enter username as "{user}" and password as "{pwd}"')
def details_enter(context,user,pwd):
    time.sleep(5)
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)

@when('click on Login button')
def login_button(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must be successfully logged in to the dashboard page')
def homepage(context):
    time.sleep(5)
    try :
        home = context.driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]")
        txt = home.text
    except :
        context.driver.close()
        assert False,"**%Login Failed%**"

    if txt == 'Employee List':
        context.driver.close()
        assert True, "%%Login Successfull%%"

