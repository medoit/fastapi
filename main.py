from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="PMS-BACKEND"
)


@app.get("/")
def hello():
    return 'Hello'

users = [
    {"id": 1, "role": "admin", "name": "Alexander"},
    {"id": 2, "role": "operator", "name": "Ivan"},
    {"id": 3, "role": "", "name": ""},
]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in users if user.get("id") == user_id]

@app.get("/users")
def get_users(limit: int = 10, offset: int = 0):
    return users[offset:][:limit]

@app.post("/users/{user_id}")
def change_user(user_id: int, new_name: str):
    _user = list(filter(lambda user: user.get("id") == user_id, users))[0]
    _user["name"] = new_name
    return {"status": 200, "data": _user}

list_passwords = []

class Password(BaseModel):
    id: int
    user_id: int
    login: str
    password: str

@app.post("/passwords")
def add_password(passwords: List[Password]):
    list_passwords.extend(passwords)
    return {"status": 200, "data": list_passwords}