import pytest


@pytest.fixture(scope="session")
def alice(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def bob(accounts):
    return accounts[1]


@pytest.fixture(scope="module")
def pennydao(alice, PennyDAO):
    return alice.deploy(PennyDAO, "Some URI")


@pytest.fixture(autouse=True)
def function_isolation(fn_isolation):
    pass