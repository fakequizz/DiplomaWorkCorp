from fastapi import APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

policies_router = APIRouter()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@policies_router.get("/", response_class=HTMLResponse)
def policies_page(request: Request):
    return templates.TemplateResponse("policies.html", {"request": request})
