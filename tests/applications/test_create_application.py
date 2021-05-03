def test_return_value(alice, applications, application_data):
    tx = applications.createApplication(application_data, {"from": alice})
    assert tx.return_value is True


def test_event_emitted(alice, applications, application_data):
    tx = applications.createApplication(application_data, {"from": alice})

    expected_values = (0, alice, 0, tx.timestamp)

    assert "ApplicationEvent" in tx.events
    assert tx.events["ApplicationEvent"] == expected_values


def test_application_owner(alice, applications, application_data):
    applications.createApplication(application_data, {"from": alice})

    assert applications.ownerOf(0) == alice
