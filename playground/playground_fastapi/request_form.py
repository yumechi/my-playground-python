from fastapi import FastAPI, Form

app = FastAPI()


# FastAPIではフォームデータを json のように内部的に扱うことができるらしいので下記の書き方ができる
# ただし Form として受け取ることを期待しているデータを Body で受け取ることはできない
# ちなみに Form データを curl で送るときは下記
# curl -X POST "http://localhost:8000/login/" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "username=%E3%81%BA%E3%81%93&password=ninjindaisuki"
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
