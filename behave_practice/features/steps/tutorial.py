from behave import given, step, then, when


@given("we have behave installed")
def installed(context):
    pass


@when("we implement a test")
def a_test(context):
    assert True is not False  # noqa: PLR0133 (behave チュートリアルのまま)


@then("behave will test it for us!")
def it_for_us(context):
    assert context.failed is False


@step("we enjoy test!")
def enjoy_test(context):
    assert bool(42) is not False
    assert bool(0) is False
