import RPi.GPIO as GPIO
import time

alarm = 1
button_ok = 2
button_1 = 3
button_2 = 4

class FME:
    def __init__(self):
        self.time_short = 0.2
        self.time_long = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(alarm, GPIO.IN)
        GPIO.setup(button_ok, GPIO.IN)
        GPIO.setup(button_1, GPIO.IN)
        GPIO.setup(button_2, GPIO.IN)

    def checkAlarm():
        return GPIO.input(alarm)

    def __press(self, button, sleepTime):
        GPIO.output(button, 1)
        time.sleep(sleepTime)
        GPIO.output(button, 0)

    def press_ok(self, short = True):
        if short == True:
            self.__press(button_ok, self.time_short)
        else:
            self.__press(button_ok, self.time_long)

    def press_1(self, short = True):
        if short == True:
            self.__press(button_1, self.time_short)
        else:
            self.__press(button_1, self.time_long)

    def press_2(self, short = True):
        if short == True:
            self.__press(button_2, self.time_short)
        else:
            self.__press(button_2, self.time_long)