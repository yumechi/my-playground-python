from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

# ファイルを Form に流し込む
# curl でやるには
# curl -X POST "http://localhost:8000/files/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@DSC_0792.jpg;type=image/jpeg"
@app.post("/file/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


# UploadFile は一時領域にファイルを書きだす（spooled）
# これにより大きいファイルも処理することが可能
# SpooledTemporaryFile も参照
# 逆に一時領域を使わずメモリに転嫁する方法もある（上の例がそう）
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


# sample では multiupload でフォーム使ってるけど、 localhost:8000/docs のもので十分
@app.post("/files/")
async def create_files(files: list[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

