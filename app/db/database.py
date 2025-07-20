
from motor.motor_asyncio import AsyncIOMotorClient
import os

client = None
db = None

async def connect_to_mongo():
    global client, db
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["hrone"]
