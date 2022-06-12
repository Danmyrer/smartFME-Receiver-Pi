import time
from datetime import datetime

from smartFME_Reciever import FME
from smartFME_Reciever import smartFME_Monitor

DELAY = 2
IST_ALARM_AKTIV = False


fme = FME.FME()
while True:
    try:
        if fme.checkAlarm() == 1:
            IST_ALARM_AKTIV=True
            break
        time.sleep(DELAY)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        break


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
if IST_ALARM_AKTIV is True:
    print(f"[FMEListener] Alarm wurde um {current_time} ausgelöst)")
    smartFME_Monitor.einsatz()
else:
    print(f"[FMEListener] Alarm wurde um {current_time} abgebrochen")