from fastmcp import FastMCP
from mcpserver.utils import get_location, search_place_with_details, Location, PlaceWithDetails

mcp = FastMCP("KakaoMap")

@mcp.tool()
async def query_location(query: str) -> dict | str:
    """Get location from query string."""
    return {}

@mcp.tool()
async def search_places(x: float, y: float, keyword: str) -> list[dict] | str:
    """Search places by keyword near the given coordinates."""
    return []

def main():
    mcp.run()

if __name__ == "__main__":
    main()
