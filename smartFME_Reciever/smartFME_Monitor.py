import asyncio
from smartFME_Reciever import payload as pl
from smartFME_Reciever import cloud

EINSATZBESCHREIBUNG = False


def einsatz():
    if EINSATZBESCHREIBUNG is False:
        payload = pl.buildPayload()
        asyncio.run(cloud.Cloud().push_payload(payload))
    else:
        raise Exception("Einsatzbeschreibungen werden noch nicht Unterstützt")


# Region debug
einsatz()
# Endregion
