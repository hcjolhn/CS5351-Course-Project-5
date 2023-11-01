from behave import *

use_step_matcher("re")


@given(": I want to validate the network traffic")
def step_impl(context):
    print("testinggg")
    for row in context.table.rows:
        assert row is not None
        print(row)

@step(": Validate now")
def step_impl(context):
    is_valid = True
    network_traffic = []
    assert context.table is not None
    for row in context.table.rows:
        for res in context.driver.requests:
            if row[0] in res.url:
                break
        else:
            is_valid = False

