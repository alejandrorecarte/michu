from fastapi import HTTPException, status
from pymongo import MongoClient
from models.users import User
import os

mongo_url = os.environ.get("MONGO_INITDB_ROOT_URL")

client = MongoClient(mongo_url)

# Create new user
def create_user(user: User):
    db = client['users']
    collection = db['users']
    if collection.find_one({"username": user.username}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    collection.insert_one(user)