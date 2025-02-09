import random
from pydantic import BaseModel
from models.users import User
from typing import List, Dict

class Dice(BaseModel):
    value: int

    def __init__(self):
        self.value = 0

    def throw(self):
        self.value = random.randint(1, 6)

class Michu(BaseModel):
    round: User
    users: List[User]
    lives: Dict[str, int]
    dices: Dict[str, List[Dice]]
    tries: Dict[str, int]

    def __init__(self, users: List[User]):
        for user in users:
            self.round = users[random.randint(0, len(users) - 1)]
            self.users = users
            self.lives[user.id] = 15
            self.dices[user.id] = [Dice(), Dice()]
            self.tries[user.id] = 3 

    def finish_turn(self, user_id: str):
        self.round = self.users[(self.users.index(self.round) + 1) % len(self.users)]
        self.tries[user_id] = 3
        return self.round.id
    
    def throw_dices(self, user_id: str, dice_left: bool, dice_right: bool):
        if self.round.id == user_id:
            if self.lives[user_id] > 0:
                if self.tries[user_id] > 0:
                    if dice_left:
                        self.dices[user_id][0].throw()
                    if dice_right:
                        self.dices[user_id][1].throw()
                self.tries[user_id] -= 1
                return self.dices[user_id][0].value, self.dices[user_id][1].value
            else:
                self.finish_turn(user_id)

    def get_dice_value(self, user_id: str):
        return self.dices[user_id][0].value, self.dices[user_id][1].value
    
    def get_lives(self):
        return self.lives
    
    def get_round(self):
        return self.round.id
    
    def get_users(self):
        return self.users