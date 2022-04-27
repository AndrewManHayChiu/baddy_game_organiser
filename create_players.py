# The purpose of this script is to fill the database with dummy data

from models import Player, PlayerTiers, Session, engine
from baddy.players import create_player, extract_player, update_player_tier

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
    {'name': 'test', 'gender': 'female', 'tier': 8},
    ]

for id, player in enumerate(players, start=1):
    if extract_player(player_id=id) is None:
        create_player(player_id=id, name=player['name'], gender=player['gender'], tier=player['tier'])
    else:
        update_player_tier(player_id=id, tier=player['tier'])