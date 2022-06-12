from unittest import mock
from unittest.mock import patch

from smartFME_Reciever import FME

# region checkAlarm
@mock.patch("smartFME_Reciever.FME.io.input", return_value=0)
def test_checkAlarm_false(mock_ioInput):
    assert FME.FME().checkAlarm() == 0



@mock.patch("smartFME_Reciever.FME.io.input", return_value=1)
def test_checkAlarm_true(mock_ioInput):
    assert FME.FME().checkAlarm() == 1
# endregion


# region press_short
@mock.patch("smartFME_Reciever.FME.FME._FME__press")
def test_press_ok_short(mock_press):
    FME.FME().press_ok()
    mock_press.assert_called_with(17, 0.2)


@mock.patch("smartFME_Reciever.FME.FME._FME__press")
def test_press_1_short(mock_press):
    FME.FME().press_1()
    mock_press.assert_called_with(27, 0.2)


@mock.patch("smartFME_Reciever.FME.FME._FME__press")
def test_press_2_short(mock_press):
    FME.FME().press_2()
    mock_press.assert_called_with(22, 0.2)
# endregion


# region press_long
@mock.patch("smartFME_Reciever.FME.FME._FME__press")
def test_press_ok_long(mock_press):
    FME.FME().press_ok(True)
    mock_press.assert_called_with(17, 1)


@mock.patch("smartFME_Reciever.FME.FME._FME__press")
def test_press_1_long(mock_press):
    FME.FME().press_1(True)
    mock_press.assert_called_with(27, 1)


@mock.patch("smartFME_Reciever.FME.FME._FME__press")
def test_press_2_long(mock_press):
    FME.FME().press_2(True)
    mock_press.assert_called_with(22, 1)
# endregion


# region press
@mock.patch("smartFME_Reciever.FME.io.output")
def test_press(mock_ioOutput):
    FME.FME()._FME__press(99, 0.1)
    mock_ioOutput.assert_called_with(99, 0)
# endregion
