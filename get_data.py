from models import Player, Session, engine

session = Session(bind=engine)

# Extract all data
# players = session.query(Player).all()

# for player in players:
#     print(player.player_id, player.name)

# Extract individual data
player = session.query(Player).filter(Player.player_id == 1).all()
print(player)