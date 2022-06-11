import pytest
from smartFME_Reciever import smartFME_Monitor as monitor


def test_einsatz_mitBeschreibung():
    with pytest.raises(Exception):
        monitor.einsatz(True)
