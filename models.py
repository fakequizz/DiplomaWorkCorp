from sqlalchemy import Column, Integer, String, Text
from database import Base  # Importing Base from database.py

class LogEntry(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    file_path = Column(String, nullable=True)
    email_content = Column(String, nullable=True)
    
class SecurityPolicy(Base):
    __tablename__ = "security_policies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="staff")  # "admin" или "staff"
