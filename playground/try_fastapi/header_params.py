from typing import Optional

from fastapi import Header, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
    himitsu_word: Optional[str] = Header(None, convert_underscores=False),
):
    """
    Headerの場合はデフォルトでハイフンからアンダースコアへの変数変換がされる。大文字小文字の違いも意識不要。
    アンダースコアを使いたい場合は convert_underscores=False を指定する必要がある。

    サンプル
    ```shell
    > curl -X GET "http://localhost:8000/items/" -H  "accept: application/json" -H "user-agent: peko" -H "himitsu_word: konpeko"
    {"User-Agent":"peko","himitsu_word":"konpeko"}%
    ```
    """
    return {"User-Agent": user_agent, "himitsu_word": himitsu_word}


@app.get("/items_2/")
async def read_items_2(x_token: Optional[list[str]] = Header(None)):
    """
    リストのサンプル。

    サンプル
    ```shell
    > curl -X GET "http://localhost:8000/items_2/" -H  "accept: application/json" -H "X-Token: peko,nanodesu"
    {"X-Token values":["peko","nanodesu"]}%
    ```
    """
    return {"X-Token values": x_token}
