from behave import *

use_step_matcher("re")

@given(": I Click on Create button")
def step_impl(context):
    context.testpage.createbtn_click()

@step(": I Click on Submit button")
def step_impl(context):
    context.testpage.submitbtn_click()

@step(': I Enter a "(?P<Name>.+)" in Name field')
def step_impl(context, Name):
    context.yoyo = "hi"
    context.testpage.input(Name,"name")

@step(': I Enter a "(?P<Email>.+)" in Email field')
def step_impl(context, Email):
    context.testpage.input(Email,"email")

@step(': I Enter a "(?P<Message>.+)" in Message field')
def step_impl(context, Message):
    context.testpage.input(Message,"message")
