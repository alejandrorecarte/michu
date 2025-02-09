from fastapi import APIRouter, HTTPException, status, Response, Depends, Request
import logging
from controllers.users import create_user
from schemas.users.requests import PostCreateUserRequest

logger = logging.getLogger(__name__)

router = APIRouter()

# Create a user
@router.post("/create", status_code=status.HTTP_201_CREATED)
def post_create(variables: PostCreateUserRequest, response: Response):
    try:
        # Call the controller
        return create_user(username= variables.username)
    except Exception as error:
        logger.warning(str(error))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )