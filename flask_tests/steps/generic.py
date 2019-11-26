from nose.tools import assert_equal, assert_true

import helper

@when(u'I get the response status code')
def step_impl(context):
    """Assign `context.verify_me` to status code of `response`"""
    try:
        context.verify_me = context.response.status_code
    except ValueError as error:
        raise error


@when(u'I get the response json')
def step_impl(context):
    """Assign `context.verify_me` to json data of `response`"""
    try:
        context.verify_me = context.response.json()
    except ValueError as error:
        raise error


@when(u'I get the response text')
def step_impl(context):
    """Assign `context.verify_me` to json data of `response`"""
    try:
        context.verify_me = context.response.content
    except ValueError as error:
        raise error


@when(u'I get the response headers')
def step_impl(context):
    """Assign `context.verify_me` to header data of `response`"""
    try:
        context.verify_me = context.response.headers
    except ValueError as error:
        raise error


@when(u'I take position "{position:d}" from the list')
def step_impl(context, position):
    """Assign `context.verify_me` to the data from a list stored in
    `context.verify_me` at a given position"""
    try:
        context.verify_me = context.verify_me[position]
    except ValueError as error:
        raise error


@when(u'I get the "{parameter}" property')
def step_impl(context, parameter):
    """Assign `context.verify_me` to a given property of what is
    currently stored in `context.verify_me`"""

    data = parameter.split()
    for parameter in data:
        try:
            context.verify_me = context.verify_me[parameter]
        except ValueError as error:
            raise error

#######################################
# assertions
###################

@then(u'the status code should be "{code:d}"')
def step_impl(context, code):
    """Verify that the status code that is stored in `context.verify_me` is the expected status code"""

    assert_equal(code, context.verify_me,
                 "Expected status code: {} | Received {}".format(
                     code, context.verify_me))


@then(u'response content type should be "{expected_content_type}"')
def step_impl(context, expected_content_type):
    """Verify that the headers stored in `context.verify_me` is the expected content type"""
    content_type = context.verify_me['Content-Type']

    assert_equal(content_type, expected_content_type,
                 "Expected content type: {} | Received: {}".format(
                     expected_content_type, content_type))


@then(u'the response should be type "{data_type}"')
def step_impl(context, data_type):
    """Verify that the response is the correct type"""
    expected_type = helper.get_type_from_string(data_type)
    received_type = type(context.verify_me)

    assert_equal(expected_type, received_type,
                 "Expected type {}, got {}".format(expected_type, received_type))


@then(u'the expected fields should be present')
def step_impl(context):
    """Verify that the object held in context.verify` me contains the given fields"""
    errors = []
    # Loop through the table rows checking each is present in the verify_me object
    for row in context.table:
        if row['field'] not in context.verify_me:
            errors.append(row['field'])

    # I would normally use the falsity of an empty list to assert against here,
    # but explicit is better than implicit
    assert_equal(len(errors), 0, "There were {} fields missing: {}".format(
                 len(errors), errors))


@then(u'the expected fields content should be the correct data type')
def step_impl(context):
    """Verify that the key values in `context.verify_me` are the expected data types"""
    errors = []

    for row in context.table:
        # First check that the key actually exists before trying to check data type
        check_exists = context.verify_me.get(row['field'])
        if check_exists is None:
            errors.append("Unable to check data type of {}, key is missing".format(row['field']))
            continue

        # Lookup for data types from string
        expected_type = helper.get_type_from_string(row['data_type'])
        received_type = type(context.verify_me.get(row['field']))

        if received_type != expected_type:
            errors.append("Expected {} value to be {} type, but it is {}".format(
                row['field'], expected_type, received_type))

    assert_equal(len(errors), 0, "There were {} errors: {}".format(
                 len(errors), errors))


@then(u'the expected fields should contain expected content')
def step_impl(context):
    """Verify the contents for the given fields matches the corresponding content of
    the object held in `context.verify_me`"""
    errors = []

    for row in context.table:
        # I can't control the content type of the table cells so everything is converted to a string
        received_content = str(context.verify_me.get(row['field']))
        if received_content is None:
            errors.append("Unable to check content of {}, key is missing".format(row['field']))
            continue

        if received_content != row['content']:
            errors.append("Expected {} content to be {}, but it is {}".format(
                row['field'], row['content'], received_content))

    assert_equal(len(errors), 0, "There were {} errors: {}".format(
                 len(errors), errors))


@then(u'the response text should read')
def step_impl(context):
    """If the response returns text this verifies the text is equal to the expected response"""

    for row in context.table:
        assert_equal(row["field"], context.verify_me,
            "{} is not equal to {}".format(row["field"], context.verify_me))


@then(u'the "{parameter}" property should contain a valid uuid4 or nil uuid')
def step_impl(context, parameter):
    """Verify that the value of a given property of the object held in
    `context.verify_me` is a valid uuid4 or nil uuid"""
    uuid = context.verify_me.get(parameter)
    if uuid is None:
        assert False, "Unable to valid uuid of {}, key missing from: {}".format(parameter, context.verify_me)

    # This will match to uuid4 with or without dashes as both are valid
    regex = re.compile(r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)

    assert_true((regex.match(uuid) or uuid == "00000000-0000-0000-0000-000000000000"),
                "{} is not a valid uuid4".format(uuid))


@then(u'the "{parameter}" property should be time formatted correctly')
def step_impl(context, parameter):
    """Verify that the value of a given property of the object held in
    `context.verify_me` is a date time format complicit with ISO8601"""
    timestamp = context.verify_me[parameter]

    # This will match all ISO8601 formatted date/time stamps
    regex = re.compile(r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|'
                       r'[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]'
                       r'+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$')

    assert_true(regex.match(timestamp),
                "{} is not time formatted correctly".format(timestamp))


@then(u'the response should have length "{expected_length}"')
def step_impl(context, expected_length):
    """Check the length of a list/string/dict in context.verify_me against a given length"""
    items_in_resp = len(context.verify_me)
    assert_equal(items_in_resp, int(expected_length),
                 "Expected {} items, there were {}:\n{}".format(expected_length, items_in_resp, context.verify_me))
