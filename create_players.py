from models import Player, Player_tiers, Session, engine

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
]

def update_player_tier(player_id, tier):
    player_tier = Player_tiers(player_id=player_id, tier=tier)
    session.add(player_tier)
    session.commit()

def create_player(name, gender):
    new_player = Player(name=name, gender=gender)
    session.add(new_player)
    session.commit()

for id, player in enumerate(players, start=1):
    create_player(name=player['name'], gender=player['gender'])
    update_player_tier(player_id=id, tier=player['tier'])