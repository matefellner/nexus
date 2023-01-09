from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world again"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
def create_item(item: Item):
    return item
