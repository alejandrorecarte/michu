from pydantic import BaseModel

class PostCreateUserRequest(BaseModel):
    username: str