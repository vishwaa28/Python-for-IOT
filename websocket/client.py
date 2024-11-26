import asyncio
import websockets
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to handle the chat client
async def chat():
    try:
        async with websockets.connect('ws://localhost:12345') as websocket:
            logging.info("Connected to server")
            while True:
                # Prompt the user for a message
                message = input("Enter message: ")
                # Send the message to the server
                await websocket.send(message)
                logging.info(f"Sent message: {message}")
                # Receive a message from the server
                response = await websocket.recv()
                print(f"Received: {response}")
    except Exception as e:
        logging.error(f"Connection failed: {e}")

# Run the client
if __name__ == "__main__":
    asyncio.run(chat())
