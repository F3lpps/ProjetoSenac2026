from http import HTTPStatus

from fastapi import FastAPI

from ViajeiAPI.schemas.user import User, UserDB, Userpublic

app = FastAPI()

database = []


@app.get('/')
def read_root():
    return {'message': '(⌐■_■)👌'}


@app.post("/auth/", status_code=HTTPStatus.CREATED, response_model=Userpublic)
def register(user: User):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
