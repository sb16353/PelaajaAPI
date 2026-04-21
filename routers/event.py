from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db.models import Event, EventIn
from db.database import get_session
from crud.event import validate_event_type
import crud.event as crud

router = APIRouter(prefix="/events", tags=["events"])

@router.get("", status_code=status.HTTP_200_OK, response_model=list[Event])
def get_events(type: str | None = None, sess: Session = Depends(get_session)) -> list[Event]:
    if type and not validate_event_type(type):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid event type")

    return crud.get_events(sess, type)
