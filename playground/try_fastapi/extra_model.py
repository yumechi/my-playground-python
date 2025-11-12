from typing import Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


"""
べた書きもできる、共通に持っていいものは共通にしてしまうのが良い

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None
"""


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    import hashlib

    s = ("supernenechi" + raw_password).encode()
    # blake2 というハッシュ形式があるので試しに使ってみる
    return hashlib.blake2b(s).hexdigest()


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    # unwrapしてマップ可能なものはマップさせてしまう、足りないものは個別に足す
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    """
    入ってくるユーザーデータモデルと、保存したいユーザーモデルと、返したいユーザーモデルが全て異なるケース
    """
    user_saved = fake_save_user(user_in)
    return user_saved


# 下記は複数の型を返すケースで、typingのUnionを活用する
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int = 1


items = {
    "item1": {"description": "PUIPUI cute car", "type": "car"},
    "item2": {
        "description": "plain not cute item",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    """
    返すモデルが一意でないパターン
    """
    return items[item_id]


all_items = [
    {"name": "nanodesu", "description": "mad"},
    {"name": "peko", "description": "funny"},
]


@app.get("/all_item", response_model=list[PlaneItem])
async def read_all_item():
    """
    listで返すパターン。 3.9 なら typing.List でなくても大丈夫
    """
    return all_items


@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    """
    dictで返すパターン。 3.9 なら typing.Dict でなくても大丈夫
    """
    return {"inu": 56.7, "neko": 2.21}
