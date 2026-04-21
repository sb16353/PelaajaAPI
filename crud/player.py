from sqlmodel import Session, select
from db.models import PlayerIn, Player

def get_players(sess: Session) -> list[Player]:
    return sess.exec(select(Player)).all()

def create_player(sess: Session, player_in: PlayerIn) -> Player:
    player = Player.model_validate(player_in)

    sess.add(player)
    sess.commit()
    sess.refresh(player)

    return player

def get_player_by_id(sess: Session, player_id: int) -> Player:
    return sess.get(Player, player_id)
