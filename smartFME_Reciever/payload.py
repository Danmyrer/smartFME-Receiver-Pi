def buildPayload(data=None):
    if data is None:
        data = "999"  # Einsatzbeschreibung unbekannt
    return '{"A_DATA":"' + data + '"}'
