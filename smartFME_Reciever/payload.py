def buildPayload(data=None):
    if data is None:
        data = "99"  # Einsatzbeschreibung unbekannt
    return '{"A_DATA":"' + data + '"}'
