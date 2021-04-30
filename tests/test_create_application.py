def test_create_application_emits_event(alice, pennydao):
    tx = pennydao.createApplication("MYIPFSCID", {"from": alice})

    assert "ApplicationCreated" in tx.events
    assert tx.events["ApplicationCreated"]["applicant"] == alice
    assert tx.events["ApplicationCreated"]["ipfsCID"] == "MYIPFSCID"
