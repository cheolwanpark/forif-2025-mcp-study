from fastmcp import FastMCP

mcp = FastMCP("Hello World")

@mcp.tool()
def hello(name: str) -> str:
    """이름을 받아서 인사하는 함수"""
    return f"Hello {name}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()