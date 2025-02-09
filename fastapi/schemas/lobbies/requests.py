from pydantic import BaseModel
from typing import List
from models.users import User

class PostCreateLobbyRequest(BaseModel):
    host: str
    name: str
    max_players: int = 4
    is_public: bool = True

class PostJoinLobbyRequest(BaseModel):
    lobby_id: str
    user_id: str

class PostLeaveLobbyRequest(BaseModel):
    lobby_id: str
    user_id: str