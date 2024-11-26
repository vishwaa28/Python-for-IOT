import asyncio
from aiocoap import *

async def coap_get_request():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri="coap://localhost:5683/resource")  # Ensure the correct port is used
    response = await protocol.request(request).response

    print(f"Response code: {response.code}")
    print(f"Response payload: {response.payload.decode('utf-8')}")

if __name__ == "__main__":
    asyncio.run(coap_get_request())  # Use asyncio.run to manage the event loop
