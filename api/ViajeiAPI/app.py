from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from ViajeiAPI.schemas.message import Message
from ViajeiAPI.schemas.user import User, UserDB, Userlist, Userpublic

app = FastAPI()

database = []


@app.get("/")
def read_root():
    return {"message": "(⌐■_■)👌"}


@app.post("/auth/", status_code=HTTPStatus.CREATED, response_model=Userpublic)
def register(user: User):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get("/users", response_model=Userlist)
def test_read_users():
    return {"users": database}


@app.delete("/users/{user_id}", response_model=Message)
def test_delete(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    del database[user_id - 1]

    return {"message": "User deleted"}
