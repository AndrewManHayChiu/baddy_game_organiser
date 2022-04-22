from models import Player, Player_tiers, Session, engine
from baddy.players import create_player, update_player_tier

session = Session(bind=engine)

players = [
    {'name': 'Andrew Chiu', 'gender': 'male', 'tier': 8},
    {'name': 'Terence Chiu', 'gender': 'male', 'tier': 8},
    {'name': 'Felix Yung', 'gender': 'male', 'tier': 8},
    {'name': 'Billy Wu', 'gender': 'male', 'tier': 8},
    {'name': 'David Yeung', 'gender': 'male', 'tier': 7},
    {'name': 'David Wei', 'gender': 'male', 'tier': 6},
    {'name': 'David Ng', 'gender': 'male', 'tier': 7},
    {'name': 'James Harnishmacher', 'gender': 'male', 'tier': 8},

for id, player in enumerate(players, start=1):
    create_player(name=player['name'], gender=player['gender'])
    update_player_tier(player_id=id, tier=player['tier'])