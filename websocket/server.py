import asyncio
import websockets
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set of connected clients
connected_clients = set()

# Function to handle each client connection
async def handle_client(websocket, path):
    logging.info(f"New client connected: {websocket.remote_address}")
    # Add the new client to the set of connected clients
    connected_clients.add(websocket)
    try:
        # Listen for messages from the client
        async for message in websocket:
            logging.info(f"Received message from {websocket.remote_address}: {message}")
            # Broadcast the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        logging.info(f"Client disconnected: {websocket.remote_address}")
    finally:
        # Remove the client from the set of connected clients
        connected_clients.remove(websocket)

# Main function to start the WebSocket server
async def main():
    logging.info("Starting server...")
    server = await websockets.serve(handle_client, 'localhost', 12345)
    logging.info("Server started on ws://localhost:12345")
    await server.wait_closed()

# Run the server
if __name__ == "__main__":
    asyncio.run(main())  # This will create a new event loop and run the server
