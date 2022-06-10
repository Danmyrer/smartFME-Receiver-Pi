import asyncio
import payload as pl
import cloud

EINSATZBESCHREIBUNG = False

def einsatz():
    if EINSATZBESCHREIBUNG == False:
        payload = pl.buildPayload()
        asyncio.run(cloud.Cloud().push_payload(payload))
    else:
        raise Exception("Einsatzbeschreibungen werden noch nicht Unterstützt")

#region debug
einsatz()
#endregion