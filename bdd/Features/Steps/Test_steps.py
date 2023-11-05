from behave import *

use_step_matcher("re")

@given(": I Click on Create button")
def step_impl(context):
    context.testpage.createbtn_click()

@step(": I Click on Submit button")
def step_impl(context):
    context.testpage.submitbtn_click()

@given(': I Click on Edit button with the "(?P<order>.+)"-th row')
def step_impl(context, order):
    context.testpage.editbtn_click(order)

@step(': I Click on Delete button with the "(?P<order>.+)"-th row')
def step_impl(context, order):
    context.testpage.delbtn_click(order)

@step(': I Click on Back button')
def step_impl(context):
    context.testpage.backbtn_click()

@step(': I Enter a "(?P<Name>.+)" in Name field')
def step_impl(context, Name):
    context.yoyo = "hi"
    context.testpage.input(Name,"name")
    context.testpage.inputValidation("name")

@step(': I Enter a "(?P<Email>.+)" in Email field')
def step_impl(context, Email):
    context.testpage.input(Email,"email")
    context.testpage.inputValidation("email")

@step(': I Enter a "(?P<Message>.+)" in Message field')
def step_impl(context, Message):
    context.testpage.input(Message,"message")

@step(': I Clear Name field')
def step_impl(context):
    context.testpage.clear("name")

@step(': I Clear Email field')
def step_impl(context):
    context.testpage.clear("email")

@step(': I Clear Message field')
def step_impl(context):
    context.testpage.clear("message")

@step(': Check the "(?P<order>.+)"-th row "(?P<Name>.+)", "(?P<Email>.+)", "(?P<Message>.+)"')
def step_impl(context, order, Name, Email, Message):
    context.testpage.check_edit_input(order, Name, Email, Message)

@step(': Check the new input "(?P<Name>.+)", "(?P<Email>.+)", "(?P<Message>.+)"')
def step_impl(context, Name, Email, Message):
    context.testpage.check_new_input(Name, Email, Message)

@step(': I wait sometime')
def step_impl(context):
    context.testpage.wait()
