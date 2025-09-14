# UV 설치 커맨드
```
# MacOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

# Project 초기화
```
uv init
```

# hello-world 예제 실행하기
mcp 서버 실행파일 설치
```
# week2/examples/hello-world 디렉토리
uv tool install .
```
gemini 세팅 파일 이렇게 수정
```
# ~/.gemini/settings.json
{
  ...
  "mcpServers": {
    ...
    "hello-world-mcp": {
      "command": "hello-world-mcp"
    }
  }
  ...
}
```
실행해서 mcp 서버 사용해보기
```
# gemini 실행
gemini
# 프롬프트 입력
> say hello to [본인 이름]! use hello world mcp.
```
<img width="800" alt="Screenshot 2025-09-14 at 1 10 25 PM" src="https://github.com/user-attachments/assets/bc956f09-caa5-4573-a845-14c71c2f685e" />


# 바이브 코딩으로 MCP 만들어보기
### 요구사항 정리
- uv 패키지매니저와 FastMCP 사용
- 6개의 tool: **hello_[language]**
- 파일 하나로 구현
- pyproject 파일에 project.scripts 섹션에 추가해서 설치 가능하도록 구성
- 지원할 언어: 한국어, 영어, 스페인어, 일본어, 독일어, 프랑스어

### 프로젝트 구현
```
# 원하는 곳에 폴더 생성, 해당 폴더 안에서
gemini
```
프롬프트 입력
```
MCP 서버 만들어줘:
- `uv init`으로 프로젝트 초기화
- FastMCP 설치, `uv add` 사용
- 하나의 MCP 서버에 6개의 tool: **hello_[language]**
- 파일 하나로 구현: main.py
- context7 이용해서 정확한 방법으로 라이브러리 사용
- pyproject 파일 project.scripts 섹션에 mcp 서버 실행파일 추가해서 설치 가능하도록 구성, 스크립트 이름: hello-multilingual
- 지원할 언어: 한국어, 영어, 스페인어, 일본어, 독일어, 프랑스어
- 주석이나 답변은 한국어로
```
### 사용해보기
gemini 세팅 파일 이렇게 수정
```
# ~/.gemini/settings.json
{
  ...
  "mcpServers": {
    ...
    "hello-multilingual": {
      "command": "hello-multilingual"
    }
  }
  ...
}
```
실행해서 mcp 서버 사용해보기
```
# gemini 실행
gemini
# mcp 서버 연결됐는지 확인
> /mcp list
# 프롬프트 입력
> say hello in various languages! use hello multilingual mcp.
```
<img width="800" alt="Screenshot 2025-09-14 at 1 44 02 PM" src="https://github.com/user-attachments/assets/e3325134-05aa-4d8f-a424-84655279f0c5" />
