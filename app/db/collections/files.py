from pydantic import Field
from typing import TypedDict
# from pymongo.asynchronous.collection import AsyncCollection
from motor.motor_asyncio import AsyncIOMotorCollection
from ..db import database


class FileSchema(TypedDict):
    name : str = Field(..., description="name of file")
    status: str = Field(..., description="status of file")
    
    
COLLECTION_NAME = "files"
files_collection :AsyncIOMotorCollection  = database[COLLECTION_NAME]