import asyncio
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

from smartFME_Reciever import key


class Cloud:
    def __init__(self):
        try:
            self.client = IoTHubDeviceClient.create_from_connection_string(key.AZURE_CONNECTION_STRING)
        except Exception as error:
            print(error.args[0])
        print("[Cloud] Client connected successfully!")

    async def push_payload(self, payload):
        message = Message(payload)
        print(f"[Cloud] Sending message: {message}")
        await self.client.send_message(message)
        print("[Cloud] Message successfully sent!")
