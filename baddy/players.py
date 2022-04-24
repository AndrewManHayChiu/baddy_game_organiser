from models import Player, PlayerTier, Session, engine
from sqlalchemy import select

session = Session(bind=engine)

def extract_player(player_id):
    result = session.query(Player).filter(Player.player_id == player_id).first()
    return(result)

def create_player(player_id, name, gender, tier):
    if extract_player(player_id=player_id) is None:
        new_player = Player(player_id=player_id, name=name, gender=gender)
        player_tier = PlayerTier(player_id=player_id, tier=tier)
        session.add(new_player)
        session.add(player_tier)
        session.commit()
        
create_player(player_id=11, name='test-2', gender='male', tier=5)

def update_player_tier(player_id, tier):
    player_tier = session.query(PlayerTier).filter(PlayerTier.player_id == player_id).first()
    player_tier.tier = tier
    session.commit()

# stmt = (
#     select(Player)
#     .join(PlayerTier)
#     .where(Player.player_id == 1)
#         )
# player = session.scalars(stmt)

extract_player(player_id=1)
stmt = select(Player).where(Player.player_id==1)
result = session.execute(stmt)
result.fetchone()
result.all()

result = session.execute(
    select(Player.name, PlayerTier.tier)
    .join(Player.player_id)
    .where(Player.player_id == 1)
)
for row in result:
    print(row)

# for player in session.scalars(stmt):
#     print(player)

# extract_player(player_id=1)