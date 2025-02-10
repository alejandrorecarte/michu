import random
import string
from pydantic import BaseModel
from typing import List, Optional
from models.michu import Michu
from models.users import User

class Lobby(BaseModel):
    id: Optional[str] = ''.join(random.choices(string.ascii_letters + string.digits, k=8)).upper()
    name: str
    max_players: int
    players: List[User] = []
    michu : Michu
    is_public: bool = True
    host : User

    def start_game(self):
        self.michu = Michu(self.players)