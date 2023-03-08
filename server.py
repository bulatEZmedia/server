from fastapi import FastAPI

from starlette import status
from starlette.responses import Response
from pydantic import BaseModel
from models import Body
from typing import List

app = FastAPI(
    title="Bulat"
)

users = [
    {"id": 2, "role": "admin", "name": "Bulat"},
    {"id": 2, "role": "ecovolounter", "name":"Ilyas"},
    {"id": 1, "role": "help", "name": "maigran"},
]

@app.get ("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user_id]

property_users = [
    {"id": 1, "level": 4},
    {"id": 2, "level": 3},
    {"id": 3, "level": 0},
]

users2 = [
    {"id": 1, "role": "admin", "name": "Bulat"},
    {"id": 2, "role": "ecovolounter", "name":"Ilyas"},
    {"id": 3, "role": "help", "name": "maigran"},
]



@app.post("/users/{user_id}")
def change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}

users3 = [
    {"id": 1, "role": "admin", "name": "Bulat"},
    {"id": 2, "role": "ecovolounter", "name":"Ilyas"},
    {"id": 3, "role": "help", "name": "maigran"},
]


class User(BaseModel):
    id: int
    role: str
    name: str


@app.post("/adduser")
def add_user(defusers: List[User]):
    users3.extend(defusers)
    return {"data": users3}