from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db.models import Player, PlayerIn, PlayerResponse, Event, EventIn
from db.database import get_session
from crud.event import validate_event_type
import crud.player as crud
import crud.event as crud_evt

router = APIRouter(prefix="/players", tags=["players"])

@router.get("", response_model=list[Player], status_code=status.HTTP_200_OK)
def get_players(sess: Session = Depends(get_session)) -> list[Player]:
    return crud.get_players(sess)

@router.post("", status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, sess: Session = Depends(get_session)):
    try:
        return crud.create_player(sess, player_in)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e))
    
def get_player_by_id_safe(id: int, sess: Session) -> PlayerResponse:
    player = crud.get_player_by_id(sess=sess, player_id=id)
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    return player

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_player_by_id(id: int, sess: Session = Depends(get_session)) -> PlayerResponse:
    return get_player_by_id_safe(id, sess)

@router.get("/{id}/events", status_code=status.HTTP_200_OK)
def get_events_by_player_id(id: int, type: str | None = None, sess: Session = Depends(get_session)) -> list[Event]:
    player = get_player_by_id_safe(id, sess)

    if type:
        if not validate_event_type(type):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid event type")
        return [x for x in player.events if x.type == type]

    return player.events

@router.post("/{id}/events", status_code=status.HTTP_201_CREATED)
def create_event_by_player_id(event_in: EventIn, id: int, sess: Session = Depends(get_session)) -> Event:
    if not get_player_by_id_safe(id, sess):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")

    if not validate_event_type(event_in.type):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid event type")

    try:
        return crud_evt.create_event(sess, id, event_in)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e))
