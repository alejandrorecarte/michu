from fastapi import APIRouter, HTTPException, status, Response, Depends, Request
import logging
from controllers.lobbies import create_lobby, join_lobby, leave_lobby
from schemas.lobbies.requests import PostCreateLobbyRequest, PostJoinLobbyRequest
logger = logging.getLogger(__name__)

router = APIRouter()

# Create a lobby
@router.post("/create", status_code=status.HTTP_201_CREATED)
def post_create(variables: PostCreateLobbyRequest, response: Response):
    try:
        # Call the controller
        return create_lobby(variables.host, variables.name, variables.max_players, variables.is_public)
    except Exception as error:
        logger.warning(str(error))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )

# Join a lobby
@router.post("/join", status_code=status.HTTP_201_CREATED)
def post_join(variables: PostJoinLobbyRequest, response: Response):
    try:
        # Call the controller
        return join_lobby(variables.lobby_id, variables.user_id)
    except Exception as error:
        logger.warning(str(error))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
    
# Leave a lobby
@router.post("/leave", status_code=status.HTTP_201_CREATED)
def post_leave(variables: PostJoinLobbyRequest, response: Response):
    try:
        # Call the controller
        leave_lobby(variables.lobby_id, variables.user_id)
    except Exception as error:
        logger.warning(str(error))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )