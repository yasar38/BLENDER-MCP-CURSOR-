import asyncio
from blender_mcp.server import main as server_main
from blender_mcp.cursor_integration import main as cursor_main

def main():
    """Entry point for the blender-mcp package"""
    # Start both the server and Cursor integration
    asyncio.run(cursor_main())
    server_main()

if __name__ == "__main__":
    main()
