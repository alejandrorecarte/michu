from fastapi import HTTPException, status
from models.lobbies import Lobby
import logging

LOBBY_NOT_FOUND = "Lobby not found"

logger = logging.getLogger(__name__)

lobbies = []

# Create new lobby
def create_lobby(host: str, lobby_name: str, max_players: int, is_public: bool):
    logger.info(f"Creating lobby {lobby_name}")
    lobby = Lobby(host=host, name=lobby_name, max_players=max_players, is_public=is_public)
    lobbies.append(lobby)
    logger.info(f"Lobby {lobby.id} created")
    return lobby

# Join a lobby
def join_lobby(lobby_id: str, user_id: str):
    lobby = get_lobby(lobby_id)
    logger.info(f"User {user_id} joining lobby {lobby_id}")

    if lobby.max_players < len(lobby.players):
        lobby.players.append(user_id)
        logger.info(f"User {user_id} joined lobby {lobby_id}")
        return lobby
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Lobby is full"
        )

# Leave a lobby
def leave_lobby(lobby_id: str, user_id: str):
    if (lobby := next((lobby for lobby in lobbies if lobby.id == lobby_id), None)) is not None:
        lobby.players.remove(user_id)
        logger.info(f"User {user_id} left lobby {lobby_id}")
        return
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=LOBBY_NOT_FOUND
    )

def start_game(lobby_id: str, user_id: str):
    if (lobby := next((lobby for lobby in lobbies if lobby.id == lobby_id), None)) is not None:
        if user_id in lobby.players:
            if user_id == lobby.host.id:
                lobby.start_game()
                logger.info(f"Game started in lobby {lobby_id}")
                return
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not in lobby"
            )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=LOBBY_NOT_FOUND
    )

def get_lobby(lobby_id: str):
    logger.debug(f"Getting lobby {lobby_id}")
    logger.debug(f"Lobbies: {lobbies}")
    for lobby in lobbies:
        if lobby.id == lobby_id:
            logger.debug(f"Lobby {lobby_id} found")
            return lobby
        
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=LOBBY_NOT_FOUND
    )