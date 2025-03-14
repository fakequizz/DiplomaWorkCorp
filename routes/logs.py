from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db
from models import LogEntry

router = APIRouter()

@router.get("/logs_page", response_class=HTMLResponse)
def logs_page(db: Session = Depends(get_db)):
    logs = db.query(LogEntry).all()
    html_content = """
    <html>
    <head>
        <title>Event Logs</title>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
    </head>
    <body>
        <h2>Journal of Events</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Event Type</th>
                <th>File Path</th>
                <th>Email Content</th>
            </tr>
    """
    for log in logs:
        html_content += f"""
            <tr>
                <td>{log.id}</td>
                <td>{log.event_type}</td>
                <td>{log.file_path if log.file_path else "N/A"}</td>
                <td>{log.email_content if log.email_content else "N/A"}</td>
            </tr>
        """
    html_content += "</table></body></html>"
    return html_content
