from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

from smartFME_Reciever import key
# from smartFME_Reciever import localkey as key

LOG = "[cloud]"


class Cloud:
    def __init__(self):
        try:
            self.client = IoTHubDeviceClient.create_from_connection_string(key.AZURE_CONNECTION_STRING)
        except Exception as error:
            print(error.args[0])
        print(f"{LOG} Client (azure) erfolgreich verbunden")

    async def push_payload(self, payload):
        message = Message(payload)
        print(f"{LOG} Nachricht wird gesendet: {message}")
        await self.client.send_message(message)
        print(f"{LOG} Nachricht wurde erfolgreich gesendet!")
        await self.client.disconnect()
        print(f"{LOG} Client (azure) erfolgreich getrennt")
