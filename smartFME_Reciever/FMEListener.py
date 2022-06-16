import time
from datetime import datetime, timezone, timedelta

from smartFME_Reciever import FME as FMEInterface
from smartFME_Reciever import smartFME_Monitor

DELAY = 2
LOG = "[FMEListener]"


class Listener:
    def __init__(self):
        print(f"{LOG} Listener wird gestartet, drücke ctrl+c zum abbrechen")
        self.__FME = FMEInterface.FME()
        self.__ist_alarm_aktiv = False

    def __getTime(self):
        timezone_offset = +2  # European-Standard-Time
        tzinfo = timezone(timedelta(hours=timezone_offset))
        return datetime.now(tzinfo)

    def __handle_break(self):
        current_time = self.__getTime().strftime("%H:%M:%S")
        if self.__ist_alarm_aktiv is True:
            print(f"{LOG} Alarm wurde um {current_time} ausgelöst")
            smartFME_Monitor.einsatz()
        else:
            print(f"{LOG} Alarm wurde um {current_time} abgebrochen")

    def listener(self):
        while True:
            try:
                if self.__FME.checkAlarm() == 1:
                    self.__ist_alarm_aktiv = True
                    break
                time.sleep(DELAY)
            except KeyboardInterrupt:
                print("Keyboard interrupt")
                break
        self.__handle_break()


if __name__ == "__main__":
    Listener().listener()
