import asyncio
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

import key

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

#region debug
def test(dummy):
    payload = '{"A_DATA":"' + dummy + '"}'
    test_Cloud = Cloud()
    asyncio.run(test_Cloud.push_payload(payload))

test("Gruppenruf-1-Weinheim-Einsatz B2.2 LKW-Brand/A61/A61 => Koblenz 316.2 - 318.2, 316.3 - 318.2/54 AK Alzey => 53 Bornheim///19:00:06 2B 19:51 10.Feb")
#endregion