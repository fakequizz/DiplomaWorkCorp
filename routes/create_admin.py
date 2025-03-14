from models import User
from database import SessionLocal
from auth import get_password_hash  # Импортируем функцию для хэширования пароля

# Создаем сессию с базой данных
db = SessionLocal()

# Хэшируем пароль
hashed_password = get_password_hash('admin')  # Замените 'admin' на нужный вам пароль

# Создаем пользователя admin
admin_user = User(username="admin", password=hashed_password, role="admin")

# Добавляем в базу данных
db.add(admin_user)
db.commit()

print("Admin user created successfully!")
