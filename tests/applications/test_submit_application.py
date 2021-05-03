import brownie
import pytest


@pytest.fixture(autouse=True)
def local_setup(alice, applications, application_data):
    applications.createApplication(application_data, {"from": alice})


def test_return_value(alice, applications):
    tx = applications.submitApplication(0, {"from": alice})

    assert tx.return_value is True


def test_event_emitted(alice, applications):
    tx = applications.submitApplication(0, {"from": alice})
    expected_value = (3, alice, 0, tx.timestamp)

    assert "ApplicationEvent" in tx.events
    assert tx.events["ApplicationEvent"] == expected_value


def test_ownership_transfers_to_grantor(alice, applications, grantor):
    applications.submitApplication(0, {"from": alice})

    assert applications.ownerOf(0) == grantor


def test_receiver_function_is_called(alice, applications, grantor):
    tx = applications.submitApplication(0, {"from": alice})
    subcall = tx.subcalls[0]
    fn_sig = "onERC721Received(address,address,uint256,bytes)"

    assert subcall["function"] == fn_sig


def test_only_application_owner_can_submit(bob, applications):
    with brownie.reverts("dev: _msgSender is not application owner"):
        applications.submitApplication(0, {"from": bob})
