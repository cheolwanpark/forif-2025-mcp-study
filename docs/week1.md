# MCP는 직접 만들어 쓰자 1주차
[<img width="1000" alt="image" src="https://github.com/user-attachments/assets/d28b070c-785a-45d8-a682-35774e5d784c" />
](https://ddboqkob.gensparkspace.com/)  
> 이미지를 클릭하면 슬라이드를 확인할 수 있습니다.

## 실습자료 - 설치방법
#### Claude Desktop
[Download Claude](https://claude.ai/download)에서 Claude Desktop 설치  
<img src="https://github.com/user-attachments/assets/e41b4c1c-f284-4ac0-bbc7-ca914759f78a" width="700" />  
> 실행 화면

#### Gemini-CLI
```bash
# npm으로 설치
npm install -g @google/gemini-cli

# brew로 설치 (MacOS)
brew install gemini-cli
```
<img width="700" alt="image" src="https://github.com/user-attachments/assets/b3474159-0107-4cc2-815a-e5a80aeebfc6" />  

Login With Google로 로그인  
만약 자동으로 나오지 않는다면 `/auth` 입력 후 Login With Google 선택

**MCP 셋업**  
[Context7 Dashboard](https://context7.com/dashboard)에서 로그인 후 API Key 복사  
**~/.gemini/settings.json**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY"]
    },
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--headless"
      ]
    }
  }
}
```

**MCP 사용해보기**  
_context7_  
```
FastMCP 써서 mcp 서버 작성하는 방법 튜토리얼 형태로 정리해줘. use context7
```
_playwright_
```
forif.org에 들어가서 화면 캡쳐해서 저장하고, '스터디 보러가기' 버튼을 눌러. 그리고 스터디 목록 정리해서 표시해줘. use playwright
```

