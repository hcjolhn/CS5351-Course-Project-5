import json

from behave import *

use_step_matcher("re")


@step(": I want to validate the network traffic")
def step_impl(context):
    assert context.table is not None
    for row in context.table.rows:
        for res in context.driver.requests:
            if row[0] in res.url and row[1] == res.method:
                break
        else:
            is_valid = False
            break
    else:
        is_valid = True
    assert is_valid


@step(": I want to validate the network traffic request and response")
def step_impl(context):
    assert context.table is not None
    for row in context.table.rows:
        for res in context.driver.requests:
            if row[0] in res.url and row[1] == res.method \
                    and eval(res.body.decode('utf-8')) == json.loads(row[2]) \
                    and int(row[3]) == res.response.status_code:
                break
        else:
            is_valid = False
            break
    else:
        is_valid = True
    assert is_valid

