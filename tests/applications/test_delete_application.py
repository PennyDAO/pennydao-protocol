import brownie
import pytest


@pytest.fixture(autouse=True)
def local_setup(alice, applications, application_data):
    applications.createApplication(application_data, {"from": alice})


def test_return_value(alice, applications):
    tx = applications.deleteApplication(0, {"from": alice})

    assert tx.return_value is True


def test_event_emitted(alice, applications):
    tx = applications.deleteApplication(0, {"from": alice})
    expected_value = (2, alice, 0, tx.timestamp)

    assert "ApplicationEvent" in tx.events
    assert tx.events["ApplicationEvent"] == expected_value


def test_retrieve_reverts(alice, applications):
    applications.deleteApplication(0, {"from": alice})

    with brownie.reverts("dev: application does not exist"):
        applications.retrieveApplication(0)


def test_only_application_owner_can_delete(bob, applications):
    with brownie.reverts("dev: _msgSender is not application owner"):
        applications.deleteApplication(0, {"from": bob})
