from sqlmodel import Session, select
from db.models import Event, EventIn

def validate_event_type(type: str) -> bool:
    return type == "level_started" or type == "level_solved"

def create_event(sess: Session, player_id: int, evt_in: EventIn) -> Event:
    event = Event.model_validate(evt_in)

    event.player_id = player_id

    sess.add(event)
    sess.commit()
    sess.refresh(event)

    return event

def get_events(sess: Session, type: str | None = None) -> list[Event]:
    statement = select(Event)

    if type:
        statement = statement.where(Event.type == type)

    return sess.exec(statement).all()

def get_events_by_player(sess: Session, evt_in: EventIn) -> list[Event]:
    statement = select(Event)

    if evt_in.type:
        statement = statement.where(Event.player_id == evt_in.player_id and Event.type == evt_in.type)
    else:
        statement = statement.where(Event.player_id == evt_in.player_id)

    return sess.exec(statement).all()