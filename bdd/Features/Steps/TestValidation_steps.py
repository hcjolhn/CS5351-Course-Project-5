from behave import *

use_step_matcher("re")

@step(': I Enter a "(?P<Name>.+)" in Name field and validate')
def step_impl(context, Name):
    print(Name)
    context.testpage.inputValidation(Name,"Name")