from fastmcp import FastMCP

mcp = FastMCP("Hello Multilingual Server")

@mcp.tool
def hello_korean() -> str:
    """
    Returns a greeting in Korean.
    """
    return "안녕하세요"

@mcp.tool
def hello_english() -> str:
    """
    Returns a greeting in English.
    """
    return "Hello"

@mcp.tool
def hello_spanish() -> str:
    """
    Returns a greeting in Spanish.
    """
    return "Hola"

@mcp.tool
def hello_japanese() -> str:
    """
    Returns a greeting in Japanese.
    """
    return "こんにちは"

@mcp.tool
def hello_german() -> str:
    """
    Returns a greeting in German.
    """
    return "Guten Tag"

@mcp.tool
def hello_french() -> str:
    """
    Returns a greeting in French.
    """
    return "Bonjour"

def main():
    mcp.run()

if __name__ == "__main__":
    main()