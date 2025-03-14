from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from models import LogEntry  # Import LogEntry from models.py

logs_router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@logs_router.get("/", response_class=HTMLResponse)
def logs_page(request: Request, db: Session = Depends(get_db)):
    logs = db.query(LogEntry).all()
    return templates.TemplateResponse("logs.html", {"request": request, "logs": logs})
