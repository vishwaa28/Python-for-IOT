import asyncio
from aiocoap import *
from aiocoap.resource import Resource, Site

class SimpleResource(Resource):
    async def render_get(self, request):
        payload = b"This is a response from the CoAP server"
        return Message(payload=payload)
async def main():
    root = Site()
    root.add_resource(['resource'], SimpleResource())

    await Context.create_server_context(root, bind=("localhost", 5683))  # Specify the port explicitly
    await asyncio.get_running_loop().create_future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
