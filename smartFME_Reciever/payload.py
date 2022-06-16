LOG = "[payload]"


def buildPayload(data=None):
    print(f"{LOG} Building Payload")
    if data is None:
        data = "99"  # Einsatzbeschreibung unbekannt
    return '{"A_DATA":"' + data + '"}'
