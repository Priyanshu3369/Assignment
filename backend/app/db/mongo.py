from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB_NAME", "multimodal_analyzer")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI is not set in environment variables")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

history_collection = db["history"]

async def init_db():
    await history_collection.create_index([("timestamp", ASCENDING)])
