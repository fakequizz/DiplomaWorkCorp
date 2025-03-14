from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse  # Добавьте этот импорт
from routes.auth import auth_router
from routes.logs import logs_router
from routes.policies import policies_router
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from fastapi.templating import Jinja2Templates  # Добавьте этот импорт
from starlette.requests import Request  # Импортируем Request
from fastapi.responses import HTMLResponse


app = FastAPI()

# Подключаем статику и шаблоны
app.mount("/static", StaticFiles(directory="static"), name="static")

# Создаем объект для работы с шаблонами
templates = Jinja2Templates(directory="templates")

# Подключаем маршруты
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(logs_router, prefix="/logs", tags=["Logs"])
app.include_router(policies_router, prefix="/policies", tags=["Policies"])

@app.get("/", response_class=HTMLResponse)  # Теперь это будет работать
async def home(request: Request):
    """Переход на страницу входа"""
    return templates.TemplateResponse("index.html", {"request": request, "error": None})

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    # Render the admin dashboard template
    return templates.TemplateResponse("admin.html", {"request": request})

Base = declarative_base()

class LogEntry(Base):
    __tablename__ = "logs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    file_path = Column(String, nullable=True)
    email_content = Column(String, nullable=True)
