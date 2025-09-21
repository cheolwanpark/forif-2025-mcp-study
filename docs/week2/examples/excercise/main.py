from fastmcp import FastMCP

app = FastMCP("Hello Multilingual MCP Server")

@app.tool
def hello_korean() -> str:
    """한국어로 인사합니다."""
    return "안녕하세요!"

@app.tool
def hello_english() -> str:
    """영어로 인사합니다."""
    return "Hello!"

@app.tool
def hello_spanish() -> str:
    """스페인어로 인사합니다."""
    return "¡Hola!"

@app.tool
def hello_japanese() -> str:
    """일본어로 인사합니다."""
    return "こんにちは！"

@app.tool
def hello_german() -> str:
    """독일어로 인사합니다."""
    return "Guten Tag!"

@app.tool
def hello_french() -> str:
    """프랑스어로 인사합니다."""
    return "Bonjour!"

if __name__ == "__main__":
    app.run()