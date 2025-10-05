import os
from motor.motor_asyncio import AsyncIOMotorClient

# IMPORTANT: use "mongo" (the service name) as host inside Docker
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://admin:admin@127.0.0.1:27017"
)

mongo_client = AsyncIOMotorClient(MONGO_URI)
database = mongo_client["mydatabase"]

# mongo -- name of container in docker-compose.yaml