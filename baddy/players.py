from models import Player, PlayerTier, Session, engine
from sqlalchemy import select

session = Session(bind=engine)

def create_player(player_id, name, gender, tier):
    if extract_player(player_id=player_id) is None:
        new_player = Player(player_id=player_id, name=name, gender=gender)
        player_tier = PlayerTier(player_id=player_id, tier=tier)
        session.add(new_player)
        session.add(player_tier)
        session.commit()

def update_player_tier(player_id, tier):
    player_tier = session.query(PlayerTier).filter(PlayerTier.player_id == player_id).first()
    player_tier.tier = tier
    session.commit()

def extract_player(player_id):
    result = session.query(Player).filter(Player.player_id == player_id).first()
    return(result)

stmt = (
    select(Player)
    .join(PlayerTiers)
    .where(Player.player_id == 1)
        )
player = session.scalars(stmt)

for player in session.scalars(stmt):
    print(player)

extract_player(player_id=1)