from typing import Optional

from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        default=None,
        min_length=3,
        max_length=50,
        # 正規表現も使える
        # regex="^fixedquery$"
    ),
):
    """
    Queryを使ったバリデーションの例。下記をはチェック。

    * 長さが3以上
    * 長さが50以下

    サンプルのregexを設定すると受け取りパターンが固定になる（文字列開始と終了が指定されているため）
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_2/")
async def read_items_2(q: str = Query("fixedquery", min_length=3)):
    """
    初期値と min_length の組み合わせ
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_3/")
async def read_items_3(q: str = Query(..., min_length=3)):
    """
    必須パラメーターを使う。
    必須とする場合は ... にする。
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_4/")
async def read_items_4(q: list[str] = Query(["foo", "bar"])):
    """
    list を使うケース。
    初期値を使わない場合は `q: list = Query[]` と書ける。
    """

    query_item = {"q": q}
    return query_item


@app.get("/items_5/")
async def read_items_5(
    q: Optional[str] = Query(
        None,
        title="クエリ文字列",
        description="これはクエリの文字列ですという説明",
        min_length=3,
    )
):
    """
    titleやdescriptionを使うと OpenAPI 側で見たときに説明が追加される。
    """

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_6/")
async def read_items_6(
    q: Optional[str] = Query(None, alias="item-query", deprecated=True)
):
    """
    aliasを使うとパラメータとして受け取るkey名を変更できる。
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_1/{item_id}")
async def read_items_id1(
    q: Optional[str] = Query(None, alias="item-query"),
    item_id: int = Path(..., title="アイテムのID"),
):
    """
    パスパラメーターに対する説明は Path を使って書く。
    パスパラメーターは常に必須なので `Path(..., title="sample title")` のようになる。

    宣言順序は入れ替え可能。OpenAPI側で見ると Path, Query の順番で並んでいるように見える。
    """
    results = {"item_id": item_id}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_2/{item_id}")
async def read_items_id2(
    *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    """
    Pythonの機能を使って、キーワード付き引数宣言で必須な形にもできる（理解が曖昧）。

    下記の機能を活用する。

    ```
    def a(*, b):
        return b

    # これはNG
    # a()
    # a(1)

    # これはOK
    a(b=12)
    a(**{"b": 41})
    ```
    """
    results = {"item_id": item_id}
    if q:
        results |= {"q": q}
    return results


@app.get("/items_3/{item_id}")
async def read_items_id3(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=1),
    q: str,
):
    """
    Integerに対するバリデーションをかける例。 ge は greater than or equal の略であるため、1以上を示す。
    他にも gt(greater than), le(less than or equal) などが使える。

    `curl http://localhost:8000/items_3/0?q=1` とするとエラーになるのを確認できる。
    """
    results = {"item_id": item_id}
    if q:
        results |= {"q": q}
    return results
