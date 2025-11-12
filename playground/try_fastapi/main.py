from enum import Enum
from typing import Optional

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 先に宣言しないと `/user/{user_id}` 側に吸収されるため、宣言順序が大事
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user_me(user_id: str):
    return {"user_id": user_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# query_params の bool は扱いが少し特殊
# Trueになる 1, True, true, on, yes（大文字小文字問わない）
# Noになる 0, False, false, off, no（実際は True にならないすべての any なパターン）
@app.get("/items/{item_id}")
async def read_item(
    item_id: int, q: Optional[str] = None, short: bool = False
):
    items = {"item_id": item_id}
    if q:
        items |= {"q": q}
    if not short:
        items |= {
            "description": "This is an amazing item that has a long description"
        }
    return items


@app.get("/items_2/{item_id}")
async def read_user_item_needy(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    items = {"item_id": item_id, "owner_id": user_id}
    if q:
        items |= {"q": q}
    if not short:
        items |= {
            "description": "This is an amazing item that has a long description"
        }
    return items


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
