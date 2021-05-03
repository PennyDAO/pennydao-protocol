import brownie
import pytest


@pytest.fixture(autouse=True)
def local_setup(alice, applications, application_data):
    applications.createApplication(application_data, {"from": alice})


def test_stored_data_updates(alice, bob, applications, application_data):
    updated_application_data = list(application_data)
    updated_application_data[1] = bob
    applications.updateApplication(0, updated_application_data, {"from": alice})

    assert applications.retrieveApplication(0) == updated_application_data


def test_event_emitted(alice, bob, applications, application_data):
    updated_application_data = list(application_data)
    updated_application_data[1] = bob
    tx = applications.updateApplication(0, updated_application_data, {"from": alice})
    expected_value = (1, alice, 0, tx.timestamp)

    assert "ApplicationEvent" in tx.events
    assert tx.events["ApplicationEvent"] == expected_value


def test_return_value(alice, bob, applications, application_data):
    updated_application_data = list(application_data)
    updated_application_data[1] = bob
    tx = applications.updateApplication(0, updated_application_data, {"from": alice})

    assert tx.return_value is True


def test_only_application_owner_can_update(bob, applications, application_data):
    updated_application_data = list(application_data)
    updated_application_data[1] = bob

    with brownie.reverts("dev: _msgSender is not application owner"):
        applications.updateApplication(0, updated_application_data, {"from": bob})
