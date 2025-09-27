# MCP는 직접 만들어 쓰자 4주차
1. API 직접 호출해보기
2. Python 노트북에서 Python으로 API 호출 실습하기
3. MCP에 연결하고 gemini를 통해 MCP 사용해보기

# API 호출해보기
## 우리가 사용할 API
**OpenStreetMap API**: 지오코딩 API, 무료로 API 키 없이 사용가능
- 지명, 랜드마크를 주소, 위/경도로 변환
**Kakao API**: 키워드 검색 endpoint 사용 예정
- 키워드, 위/경도로부터 주변 가게 정보를 제공

## Insomnia로 실습
멘토가 화면으로 보여줄 예정, 만약 직접 해보고 싶다면
1. [Insomnia](https://insomnia.rest/) 설치
2. 'api-calls.yaml' 파일 임포트
3. Get Location 요청 Params에서 q 값 바꾸면서 실험해보기
4. Keyword Search 요청 Headers 안의 'Authorization' 값의 '<API_KEY>' 부분 자기 API 키로 바꾸기
5. query, x(lon), y(lat) 값 넣고 실험해보기, lat, lon 값은 Get Location 요청에서 돌아온 값 사용

# Python 노트북에서 Python으로 API 호출 실습
1. week4 디렉토리 (이 디렉토리) vscode 로 열기
2. 상단 메뉴 Terminal/New Terminal로 터미널 열기
2. `uv sync` 입력, 패키지 설치 확인
3. [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 설치
5. 'map_api.ipynb' 파일 vscode에서 열기
6. 자기 API 키로 KAKAO_API_KEY 입력
7. 첫번째 셀 실행, Python Interpreter로 .venv 선택(같은 디렉토리)
8. 나머지 셀 실행, 호출 파라미터 바꾸면서 실행

# MCP에 연결하고 gemini를 통해 MCP 사용해보기
1. 'mcpserver/utils.py' 내용 확인 - 파이썬 노트북과 동일
2. 'mcpserver/main.py'에 구현되지 않은 부분 채우기
3. `uv tool install --reinstall .` 커맨드로 설치 - 오류 없는 것 확인!
4. `map-mcp` 커맨드 입력해서 실행되는지 확인
5. '~/.gemini/settings.json' mcpServers 수정 - windows 는 C:\\Users\\<사용자 이름!>\\.gemini\\settings.json
```json
{
  ...
  "mcpServers": {
    ...
    "kakaomap": {
      "command": "map-mcp"
    }
  }
  ...
}
```
6. `gemini` 커맨드로 gemini 실행 후 MCP 연결 확인 - `/mcp` 입력
7. 프롬프트 입력해서 잘 동작하는지 확인하기!
- 강남역 근처 맛집 찾아줘
- 왕십리역 근처 카페, 별점 4점 이상인 곳 찾아줘