from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"ninjin": "こうぶつ！"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="存在しないアイテムぺこ",
            headers={"X-Error": "Item not exists"},
        )
    return {"items": items[item_id]}


@app.get("/items_2/{item_id}")
async def read_item(item_id: int):
    if item_id == '7':
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"items": item_id}




class RetiredException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(RetiredException)
async def unicorn_exception_handler(request: Request, exc: RetiredException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"{exc.name} の名前は禁止されている…"
        },
    )


@app.get("/vtuber/{name}")
async def read_vtuber(name: str):
    if name == "aloe":
        raise RetiredException(name=name)
    return {"vtuber_name": name}
