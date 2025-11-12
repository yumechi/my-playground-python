from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


class ItemOut(BaseModel):
    name: str
    price: float
    tax: Optional[float] = None


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2,
    },
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": [],
    },
}


# 同じモデルを返す
@app.post("/items/", response_model=ItemIn)
async def create_item(item: ItemIn):
    return item


@app.post("/items_2/", response_model=ItemOut)
async def create_item_2(item: ItemIn):
    # 出力モデルで宣言されていないものは Pydantic ですべてフィルタされる
    return item


@app.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
)
async def get_item(item_id: str):
    # response_model_exclude_unset を使うと、デフォルト値含めキーが含まれないものはは返さない
    # デフォルト値が多いものを返す時などに活用するとよい
    # bazの例のように明示的に記載がある場合は返す
    # response_model_includeで指定したキーを追加、response_model_excludeで指定したキーを削除もできる
    return items[item_id]
