from fastapi import APIRouter, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from models import User
from passlib.context import CryptContext  # Для хэширования пароля

# Инициализация маршрутов и шаблонов
auth_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Хэширование пароля
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """Хэшируем пароль перед сохранением в БД"""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Проверяем, совпадает ли введённый пароль с хэшированным"""
    return pwd_context.verify(plain_password, hashed_password)

def get_db():
    """Создаём подключение к БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Отображаем страницу входа"""
    return templates.TemplateResponse("index.html", {"request": request, "error": None})

@auth_router.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    print(f"Attempting login for {username}")  # Логируем попытку входа
    user = db.query(User).filter(User.username == username).first()
    
    if user:
        print(f"User found: {user.username}")  # Логируем, что пользователь найден
    if user and verify_password(password, user.password):
        print("Login successful!")
        return RedirectResponse(url="/admin", status_code=303)  # Переход на админку
    # print("Invalid credentials")  # Убираем сообщение об ошибке
    return templates.TemplateResponse("index.html", {"request": request, "error": None})  # Убираем ошибку
