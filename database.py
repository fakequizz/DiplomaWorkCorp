from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Убедись, что строка подключения не содержит спецсимволов
DATABASE_URL = "postgresql://postgres:newpassword@localhost:5432/DLP_logs"

# Создание движка SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  # echo=True для отладки, потом можно убрать

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
