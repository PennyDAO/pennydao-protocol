def test_return_value(alice, applications, application_data):
    applications.createApplication(application_data, {"from": alice})
    return_value = applications.retrieveApplication(0)

    assert return_value == application_data
