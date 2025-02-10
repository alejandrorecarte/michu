from fastapi import HTTPException, status
from models.users import User
from database import create_user
import logging
import hashlib

logger = logging.getLogger(__name__)


# Hash password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Create new lobby
def create_user(email: str, username: str, password: str):
    user = User(email = email, username=username, hash_password= hash_password(password))
    create_user(user)
    return user