import pytest


@pytest.fixture(scope="module")
def alice(accounts):
    return accounts[0]


@pytest.fixture(scope="module")
def bob(accounts):
    return accounts[1]


@pytest.fixture(scope="module")
def charlie(accounts):
    return accounts[2]


@pytest.fixture(scope="module")
def openzeppelin(pm):
    return pm("OpenZeppelin/openzeppelin-contracts@4.1.0")


@pytest.fixture(autouse=True)
def isolation_setup(fn_isolation):
    pass


@pytest.fixture(scope="module")
def token(alice, openzeppelin):
    return alice.deploy(openzeppelin.ERC20Mock, "Test Token", "TST", alice, 10 ** 18)


@pytest.fixture(scope="module")
def grantor(alice, openzeppelin, web3):
    fn_sig = "onERC721Received(address,address,uint256,bytes)"
    return_value = web3.keccak(text=fn_sig)[:4]
    return alice.deploy(openzeppelin.ERC721ReceiverMock, return_value, 0)


@pytest.fixture(scope="module")
def ipfs_cid():
    return "ipfs://bafybeigrf2dwtpjkiovnigysyto3d55opf6qkdikx6d65onrqnfzwgdkfa"


@pytest.fixture(scope="module")
def application_data(alice, ipfs_cid, token):
    return (token, alice, 100 * 10 ** 18, ipfs_cid)


@pytest.fixture(scope="module")
def trusted_forwarder(alice, openzeppelin):
    return alice.deploy(openzeppelin.MinimalForwarder)


@pytest.fixture(scope="module")
def applications(alice, grantor, trusted_forwarder, Applications):
    return alice.deploy(Applications, grantor, trusted_forwarder)
