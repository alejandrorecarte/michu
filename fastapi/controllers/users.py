from fastapi import HTTPException, status
from models.users import User
import logging

logger = logging.getLogger(__name__)

users = []

# Create new lobby
def create_user(username: str):
    user = User(username=username)
    users.append(user)
    return user

def get_user (user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )