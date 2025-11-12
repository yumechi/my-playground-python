from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    # Config を定義するパターン
    class Config:
        schema_extra = {
            "example": {
                "name": "Config sample",
                "description": "A very nice Item by Config Class",
                "price": 66.4,
                "tax": 7.5,
            }
        }


class Item2(BaseModel):
    # Field で書いていくパターン
    name: str = Field(..., example="Field sample")
    description: Optional[str] = Field(
        None, example="A very nice Item by Field Class"
    )
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items_2/{item_id}")
async def update_item_2(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items_3/{item_id}")
async def update_item_3(
    item_id: int,
    item: Item = Body(
        ...,
        # このあたりは JSON Schema(examples) と OpenAPI(example) で揺れがあるらしい
        example={
            "name": "arguments Foo",
            "description": "A very nice Item by arguments",
            "price": 943.3,
            "tax": 55.5,
        },
    ),
):
    # 引数内の Body で示すパターン
    results = {"item_id": item_id, "item": item}
    return results
