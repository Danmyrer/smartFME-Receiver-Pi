def buildPayload(data = None):
    if data == None:
        data = "99" #Einsatzbeschreibung unbekannt 
    return '{"A_DATA":"' + data + '"}'