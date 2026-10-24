from behave import given, step, then, when


@given("a sample text loaded into the frobulator")
def context_text_text(context):
    assert context.text is not None


@when("we activate the frobulator")
def activate_forbulator(context):
    pass


@then("we will find it similar to English")
def find_it_similar(context):
    pass


@given("a set of specific users")
def specific_users(context):
    # refs: https://behave.readthedocs.io/en/latest/api.html?highlight=table#behave.runner.Context.table
    response = []
    for row in context.table:
        assert row["name"] is not None
        assert row["department"] is not None
        assert row.get("floor") is None
        response.append(
            {
                "name": row["name"],
                "department": row["department"],
            }
        )
    context.response = response


@when("we count the number of people in each department")
def count_people(context):
    pass


@then('we will find two people in "Silly Walks"')
def find_silly_walks(context):
    assert (
        len([1 for row in context.response if row["department"] == "Silly Walks"]) == 2
    )


@step('we will find one person in "Beer Cans"')
def not_find_beer_cans(context):
    assert len([1 for row in context.response if row["department"] == "Beer Cans"]) == 1
