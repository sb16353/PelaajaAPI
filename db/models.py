from sqlmodel import SQLModel, Field, TIMESTAMP, Column, text, Relationship, JSON
from datetime import datetime, timezone

class PlayerBase(SQLModel):
    name: str

class PlayerIn(PlayerBase):
    pass

class Player(PlayerBase, table=True):
    id: int = Field(default=None, primary_key=True)
    events: list["Event"] = Relationship(back_populates="player")

class EventBase(SQLModel):
    type: str = Field(default="")
    detail: str = Field(default="")

class EventIn(EventBase):
    pass

class Event(EventBase, table=True):
    player_id: int = Field(default=None, foreign_key="player.id")
    player: Player = Relationship(back_populates="events")  
    id: int = Field(default=None, primary_key=True)
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column = Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("now()")
        )
    )

class EventsResponseBase():
    events: list[Event] = Field(default=None, sa_column=Column(JSON))

class PlayerResponse(EventsResponseBase, Player, table=False):
    pass
