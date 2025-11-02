from fastmcp import FastMCP
from mcpserver.utils import get_location, search_place, Location, PlaceWithDetails
from dataclasses import asdict

mcp = FastMCP("KakaoMap")

@mcp.tool()
async def query_location(query: str) -> dict | str:
    """Get location from query string."""
    location = get_location(query)
    return asdict(location)

@mcp.tool()
async def search_places(x: float, y: float, keyword: str) -> list[dict] | str:
    """Search places by keyword near the given coordinates."""
    places = search_place(keyword, Location(lat=y, lon=x, name=""))
    result = []
    for place in places:
        result.append(asdict(place))
    return result

def main():
    mcp.run()

if __name__ == "__main__":
    main()
