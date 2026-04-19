from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from datetime import datetime
import uuid

load_dotenv()

app = FastAPI()
router = APIRouter(prefix="/api")

client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
db = client[os.getenv("DB_NAME")]

@app.get("/")
async def root():
    return {"message": "CalmTrust API"}

@router.post("/analytics/quiz-completion")
async def quiz_completion(data: dict):
    doc = {
        "id": str(uuid.uuid4()),
        "sleep_type": data.get("sleep_type"),
        "timestamp": datetime.utcnow()
    }
    await db.quiz.insert_one(doc)
    return {"success": True}

@router.get("/analytics/stats")
async def stats():
    count = await db.quiz.count_documents({})
    return {"total_sessions": count}

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
