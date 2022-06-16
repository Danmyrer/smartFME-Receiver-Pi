import asyncio
import time

from smartFME_Reciever import payload as pl, cloud, FMEListener, FME

LOG = "[smartFME_Monitor]"


def einsatz(einsatzbeschreibung=False):
    print(f"{LOG} Einsatzroutine wurde gestartet")

    fme = FME.FME()

    if einsatzbeschreibung is False:
        print(f"{LOG} Es ist keine Einsatzbeschreibung vorhanden")
        payload = pl.buildPayload()
        asyncio.run(cloud.Cloud().push_payload(payload))

        if fme.checkAlarm() == 1:
            print(f"{LOG} Bitte beende den Einsatz auf dem FME (den großen Knopf drücken), um das Monitoring wieder aufzunehmen")
            while fme.checkAlarm() == 1:
                time.sleep(1)

        print(f"{LOG} Einsatz abgewickelt, starte Listener...")
        FMEListener.Listener().listener()
    else:
        raise Exception("Einsatzbeschreibungen werden noch nicht Unterstützt")


if __name__ == "__main__":
    einsatz()
