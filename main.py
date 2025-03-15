from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse  
from routes.auth import auth_router
from routes.logs import logs_router
from routes.policies import policies_router
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from fastapi.templating import Jinja2Templates 
from starlette.requests import Request  
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(logs_router, prefix="/logs", tags=["Logs"])
app.include_router(policies_router, prefix="/policies", tags=["Policies"])

@app.get("/", response_class=HTMLResponse)  
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "error": None})

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


Base = declarative_base()

class LogEntry(Base):
    __tablename__ = "logs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    file_path = Column(String, nullable=True)
    email_content = Column(String, nullable=True)
