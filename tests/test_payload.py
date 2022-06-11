from smartFME_Reciever import payload


def test_buildPayload_empty():
    assert payload.buildPayload() == '{"A_DATA":"99"}'


def test_buildPayload_filled():
    assert payload.buildPayload("testtesttest") == '{"A_DATA":"testtesttest"}'
