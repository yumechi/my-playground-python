from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    # これまでやってきた Query, Path, Body のようなバリデーション用の機能や、説明を入れる機能を有した Field がある
    # JSON Ｓchema に活用される
    description: Optional[str] = Field(
        None, title="商品の説明", max_length=300
    )
    price: float = Field(..., gt=0, description="価格は0円より大きくしてください")
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
