from pydantic import BaseModel

class PostCreateUserRequest(BaseModel):
    email: str
    username: str
    password: str