# Домашнее задание по теме "Основы Fast Api и маршрутизация  module_16_1.py stop


from fastapi import FastAPI
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Главная страница"}

# Создаem маршрут к странице администратора - "/user/admin".
@app.get("/user/admin")
async def read_root():
    return {"message": "Вы вошли как администратор"}

# GET-запрос — получение данных:
@app.get("/user/{user_id}")
async def read_id(user_id: int):
    return {"Вы вошли как пользователь № <user_id>": user_id}

# GET-запрос — получение данных:
@app.get("/user")
async def read_nam():
    return {"Информация о пользователе. Имя: <username>, Возраст: <age>" }