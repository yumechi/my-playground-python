from fastapi import FastAPI, status

app = FastAPI()

# httpsのコードは各種見るとこんなかんじ
# cpython: https://github.com/python/cpython/blob/61ac612e78e4f2625977406fb6f366e0a644673a/Lib/http/__init__.py
# starlette: https://github.com/encode/starlette/blob/e4307065ea6dbe708fba9643d14fe7adfff06d46/starlette/status.py
# FastAPIのstatusはstarletteのものを参照している https://github.com/tiangolo/fastapi/blob/5614b94ccc9f72f1de2f63aae63f5fe90b86c8b5/fastapi/__init__.py#L5
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
