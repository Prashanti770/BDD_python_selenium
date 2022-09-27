# import time
#
# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @given('launch browser')
# # @given('Launch Chrome Browser') #if we write previous/same scenario text -it shows "has already been defined in Existing step"
# # @given('I launch browser') #when changed to another sentence, shows undefined steps &  raise NotImplementedError(u'STEP: Given I launch browser')
# def launchbrowser(context):
#     # context.driver = webdriver.Chrome(ChromeDriverManager().install())
#     context.driver = webdriver.Chrome()
#     context.driver.implicitly_wait(5)
#
# @when('I Open OrangeHrm page')
# def openurl(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/")
#
#
# @when('enter username as "{user}" and password as "{pwd}"')
# def details_enter(context,user,pwd):
#     time.sleep(5)
#     context.driver.find_element(By.NAME,"username").send_keys(user)
#     context.driver.find_element(By.NAME, "password").send_keys(pwd)
#
# @when('click on Login button')
# def login_button(context):
#     context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
#
# @then('User must be successfully logged in to the dashboard page')
# def homepage(context):
#     time.sleep(5)
#     home = context.driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]")
#     txt = home.text
#     if txt == 'Employee List':
#         print("Success")
#     else:
#         print("Failed")
#
#
#
# # To include arguments/parameters in steps- keep it in {}