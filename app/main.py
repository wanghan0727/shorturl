from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="../templates")

# 首頁：顯示表單
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 結果頁：顯示輸入的文字
@app.post("/result", response_class=HTMLResponse)
async def result(request: Request, url: str = Form(...)):
    return templates.TemplateResponse("result.html", {"request": request, "submitted_url": url})
