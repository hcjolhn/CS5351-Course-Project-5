from behave import *

use_step_matcher("re")

@step(': I Enter a "(?P<Name>.+)" in Name field and validate')
def step_impl(context, Name):
    context.testpage.input(Name,"name")
    context.testpage.inputValidation("name")

@step(': I Enter a "(?P<Email>.+)" in Email field and validate')
def step_impl(context, Email):
    context.testpage.input(Email,"email")
    context.testpage.inputValidation("email")

@step(": I Click on Submit button with error")
def step_impl(context):
    context.testpage.submitbtn_click()