from behave import given, then, when


@given("I put {thing} in a blender,")
def given_something_test(context, thing):
    assert thing is not None
    context.thing = thing


@when("I switch the blender on")
def switch_blender(context):
    pass


@then("it should transform into {}")
def transform(context, other_thing):
    assert other_thing != context.thing
