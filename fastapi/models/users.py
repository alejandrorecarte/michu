from typing import Optional
from pydantic import BaseModel, Field
import uuid

class User(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str