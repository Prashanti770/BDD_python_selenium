import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('Launch Chrome Browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('open HRM page')
def openpage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")



@then('verfiy that logo present o page')
def verifylogo(context):
    time.sleep(5)
    status = context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']//img").is_displayed()
    if status == True:
        print("Logo is displayed")
    else:
        print("NO Logo")

@then('close Browser')
def close(context):
    # context.driver.close()
    print("close")
# Execution command :  behave features\OrangeHRM.feature
# when executed feature file, steps will be automatically executed
# This is how we will automate behave using selenium
# How we pass parameters to the steps