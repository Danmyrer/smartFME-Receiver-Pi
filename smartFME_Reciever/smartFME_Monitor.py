import asyncio

from smartFME_Reciever import payload as pl
from smartFME_Reciever import cloud
from smartFME_Reciever import FMEListener

LOG = "[smartFME_Monitor]"


def einsatz(einsatzbeschreibung=False):
    print(f"{LOG} Einsatzroutine wurde gestartet")
    if einsatzbeschreibung is False:
        print(f"{LOG} Es ist keine Einsatzbeschreibung vorhanden")
        payload = pl.buildPayload()
        asyncio.run(cloud.Cloud().push_payload(payload))

        print(f"{LOG} Einsatz abgewickelt, starte Listener...")
        FMEListener.Listener().listener()
    else:
        raise Exception("Einsatzbeschreibungen werden noch nicht Unterstützt")
