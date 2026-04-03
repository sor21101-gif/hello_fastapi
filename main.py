# main.py
# uvicorn main:app --reload <<< 로 실행
# 오류가 있을경우 :
#               폴더 위치가 있는지
#               오타가 있는지
#               자동저장이 되어있는지 

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# FastAPI 객체를 만들고
app=FastAPI()

# templates 폴더 연결 (Jinja2 를 사용해서 응답하기 위함)
templates = Jinja2Templates(directory="templates")

# 클라이언트가 "/" 최상위 경로 요청을 해오면 응답할 내용
@app.get("/", response_class=HTMLResponse)
def home(request:Request):
    # jinja2 템플릿 엔진이 index.html 문서를 읽어서 그대로 출력하는게 아닌
    # 해석한 결과를 클라이언트 웹 브라우저에 응답한다.
    result = templates.TemplateResponse("index.html", {
        "request": request,
        "fortuneToday": "동쪽으로 가면 귀인을 만나요"
    })
    return result