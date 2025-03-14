from models import User
from database import SessionLocal
from passlib.context import CryptContext  # Для хеширования пароля

# Настройка bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

# Открываем сессию
db = SessionLocal()

# Хешируем пароль перед сохранением
hashed_password = get_password_hash("admin")

# Создаем пользователя
admin_user = User(username="admin", password=hashed_password, role="admin")

# Добавляем в БД
db.add(admin_user)
db.commit()

print("✅ Админ успешно добавлен!")
