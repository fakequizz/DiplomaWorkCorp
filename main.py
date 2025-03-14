from fastapi import FastAPI, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, LogEntry
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Подключаем HTML-шаблоны
templates = Jinja2Templates(directory="templates")

# Функция для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Главная страница (вход)
@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Проверка логина
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin123":
        return RedirectResponse(url="/logs_page", status_code=303)
    else:
        return RedirectResponse(url="/", status_code=303)

# Журнал событий
@app.get("/logs_page", response_class=HTMLResponse)
def logs_page(request: Request, db: Session = Depends(get_db)):
    logs = db.query(LogEntry).all()
    return templates.TemplateResponse("logs.html", {"request": request, "logs": logs})
