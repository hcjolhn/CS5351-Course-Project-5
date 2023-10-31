from behave import *

use_step_matcher("re")


@given(": I want to validate the network traffic")
def step_impl(context):
    print("testinggg")
    for row in context.table:
        print(row)