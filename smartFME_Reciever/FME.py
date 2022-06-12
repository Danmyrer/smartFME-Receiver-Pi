import RPi.GPIO as io
import time

alarm = 1
button_ok = 2
button_1 = 3
button_2 = 4


class FME:
    def __init__(self):
        self.time_short = 0.2
        self.time_long = 1

        io.setmode(io.BCM)
        io.setwarnings(False)

        io.setup(alarm, io.IN)
        io.setup(button_ok, io.OUT)
        io.setup(button_1, io.OUT)
        io.setup(button_2, io.OUT)

    def checkAlarm(self):
        return io.input(alarm)

    def __press(self, button, sleepTime):
        io.output(button, 1)
        time.sleep(sleepTime)
        io.output(button, 0)

    def press_ok(self, short=True):
        if short is True:
            self.__press(button_ok, self.time_short)
        else:
            self.__press(button_ok, self.time_long)

    def press_1(self, short=True):
        if short is True:
            self.__press(button_1, self.time_short)
        else:
            self.__press(button_1, self.time_long)

    def press_2(self, short=True):
        if short is True:
            self.__press(button_2, self.time_short)
        else:
            self.__press(button_2, self.time_long)
