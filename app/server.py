from fastapi import FastAPI, UploadFile
from uuid import uuid4
import os   # 👈 you need this
from .utils.file import save_to_disk
from .db.collections.files import files_collection, FileSchema

app = FastAPI()

UPLOAD_DIR = "/mnt/uploads"  

@app.get("/")
def hello():
    return {"status": "healthy"}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    # id = uuid4()
    
    db_file = await files_collection.insert_one(
        document = FileSchema(
            name = file.filename,
            satus="saving"
        )
    )
    
    
    
    upload_subdir = os.path.join(UPLOAD_DIR, str(id))
    os.makedirs(upload_subdir, exist_ok=True)
    
    file_path = f"/mnt/uploads/{str(db_file.inserted_id)}/{file.filename}"

    # Save the uploaded file to disk
    await save_to_disk(file=await file.read(), path=file_path)
    
    print("push file to queue")
    
    await files_collection.update_one(
        {
            "_id": db_file.inserted_id
        },{
            "$set":{
                "status":"saved"
            }
        }
    )

    return {"file_id": str(db_file.inserted_id), "file_path": file_path}
