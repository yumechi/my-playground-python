from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    """
    複数の body を利用するケース。下記の body を送り付ける。

    ```
    {
        "item": {
            "name": "birthday voice",
            "description": "birthday special voice",
            "price": 1003.0,
            "tax": 3.2
        },
        "user": {
            "username": "pomechi",
            "full_name": "pomechi senri"
        }
    }
    ```

    """
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@app.put("/items_2/{item_id}")
async def update_item_2(
    *,
    item_id: int,
    item: Item,
    user: User,
    importtance: int = Body(..., gt=0),
    # 意図的に Body と書いてない場合は Query として解釈される
    q: Optional[str] = None,
):
    """
    Modelとは別にBodyとして受け取る値を定義するケース。
    """
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importtance": importtance,
    }
    if q:
        results |= {"q": q}
    return results


@app.put("/items_3/{item_id}")
async def update_item_3(
    *,
    item_id: int,
    item: Item = Body(..., embed=True)
):
    """
    FastAPIはデフォルトでは body をダイレクトに見るが、このケースでは `"item"` をキーとして、
    その中に body を書く形式にできる。（Multi bodyのケースでやったような形式で書ける）
    """
    results = {
        "item_id": item_id,
        "item": item,
    }
    return results
