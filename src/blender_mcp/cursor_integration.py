import asyncio
import websockets
import json
from typing import Dict, Any
from .server import main as server_main

class CursorIntegration:
    def __init__(self):
        self.server = None
        self.websocket = None
        self.is_running = False

    async def start(self, port: int = 8765):
        """Start the Cursor integration server"""
        self.is_running = True
        self.server = await websockets.serve(
            self.handle_connection,
            "localhost",
            port
        )
        print(f"Cursor integration server started on port {port}")

    async def stop(self):
        """Stop the Cursor integration server"""
        self.is_running = False
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        if self.websocket:
            await self.websocket.close()

    async def handle_connection(self, websocket, path):
        """Handle incoming WebSocket connections"""
        self.websocket = websocket
        try:
            async for message in websocket:
                await self.process_message(message)
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
        finally:
            self.websocket = None

    async def process_message(self, message: str):
        """Process incoming messages from Cursor"""
        try:
            data = json.loads(message)
            command = data.get("command")
            
            if command == "start_blender":
                # Start the Blender MCP server
                server_main()
                await self.send_response({"status": "success", "message": "Blender MCP server started"})
            elif command == "stop_blender":
                # Stop the Blender MCP server
                await self.send_response({"status": "success", "message": "Blender MCP server stopped"})
            else:
                await self.send_response({"status": "error", "message": f"Unknown command: {command}"})
        except Exception as e:
            await self.send_response({"status": "error", "message": str(e)})

    async def send_response(self, response: Dict[str, Any]):
        """Send a response back to Cursor"""
        if self.websocket:
            await self.websocket.send(json.dumps(response))

async def main():
    """Main entry point for Cursor integration"""
    integration = CursorIntegration()
    await integration.start()
    
    try:
        while integration.is_running:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await integration.stop()

if __name__ == "__main__":
    asyncio.run(main()) 