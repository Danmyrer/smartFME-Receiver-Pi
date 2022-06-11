import asyncio
from smartFME_Reciever import payload as pl
from smartFME_Reciever import cloud

def einsatz(einsatzbeschreibung = False):
    if einsatzbeschreibung is False:
        payload = pl.buildPayload()
        asyncio.run(cloud.Cloud().push_payload(payload))
    else:
        raise Exception("Einsatzbeschreibungen werden noch nicht Unterstützt")
