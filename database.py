from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к базе данных
DATABASE_URL = "postgresql://postgres:newpassword@localhost:5432/DLP_logs"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель таблицы логов
class LogEntry(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    file_path = Column(String, nullable=True)
    email_content = Column(String, nullable=True)

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)
