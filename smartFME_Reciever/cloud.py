from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

from smartFME_Reciever import key
# from smartFME_Reciever import localkey as key

LOG = "[cloud]"


class Cloud:
    def __init__(self):
        self.connection = False
        try:
            self.client = IoTHubDeviceClient.create_from_connection_string(key.AZURE_CONNECTION_STRING)
            self.connection = True
            print(f"{LOG} Client erfolgreich verbunden")
        except Exception as error:
            print(f"{LOG} " + error.args[0])
            print(f"{LOG} Verbindung zu Client konnte nicht hergestellt werden!")

    async def push_payload(self, payload):
        if self.connection is not True:
            print(f"{LOG} Ohne Verbindung kann auch keine Nachricht gesendet werden!")
            return False
        message = Message(payload)
        print(f"{LOG} Nachricht wird gesendet: {message}")
        await self.client.send_message(message)
        print(f"{LOG} Nachricht wurde erfolgreich gesendet!")
        await self.client.disconnect()
        print(f"{LOG} Client (azure) erfolgreich getrennt")
