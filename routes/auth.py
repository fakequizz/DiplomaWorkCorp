from fastapi import APIRouter, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def login_page():
    return """
    <html>
    <head>
        <title>Login</title>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
    </head>
    <body>
        <div class="login-container">
            <h2>Login</h2>
            <form method="post" action="/login">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <button class="btn" type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    """

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if user:
        if user.role == "admin":
            return RedirectResponse(url="/admin_dashboard", status_code=303)
        else:
            return RedirectResponse(url="/staff_dashboard", status_code=303)
    return "Invalid credentials. Try again."
