from fastmcp import FastMCP

mcp = FastMCP("Hello World")

@mcp.tool()
def get_location(query: str) -> str:
    """Get location from query string."""
    return {
        "x": 0.0,
        "y": 0.0,
        "name": "",
    }

@mcp.tool()
def search_places(x: float, y: float, keyword: str) -> list[dict]:
    """Search places by keyword near the given coordinates."""
    return [
        {
            "name": "",
            "category": "",
            "phone": "",
            "rating": "",
            "status": "",
            "review_count": 0,
        }
    ]

def main():
    mcp.run()

if __name__ == "__main__":
    main()
