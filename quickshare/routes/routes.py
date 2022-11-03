import shutil

from fastapi import APIRouter, File, UploadFile

route = APIRouter()


@route.get("/{file_id}")
async def download_file(file_id):
    pass


@route.put("/up")
def upload_file(file: UploadFile = File(...)):
    try:
        with open(file.filename, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        return {"message": "Upload Error"}
    finally:
        file.file.close()
    return {"message": f"Successfully uploaded {file.filename}"}
