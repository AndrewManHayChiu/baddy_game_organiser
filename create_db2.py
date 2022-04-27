from models import Player, PlayerTier, Venue, Social, Session, engine, Base
from baddy.players import create_player, extract_player, update_player_tier

# Create sqlite database and generate the schema (defined in models)
Base.metadata.create_all(engine)

# Connect to sqlite database
session = Session(bind=engine)  

# Generate dummy data
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
        create_player(player_id=id, 
                      name=player['name'], 
                      gender=player['gender'], 
                      tier=player['tier'])
    else:
        update_player_tier(player_id=id, tier=player['tier'])
        
venues = [
    {'venue_id': 1, 'name': 'DTBA'},
    {'venue_id': 2, 'name': 'Mitcham Badminton Centre'},
    {'venue_id': 3, 'name': 'MBC'}
]

for venue in venues:
    pass

socials = [
    {'social_id': 1, 
     'venue_id': 1, 
     'social_name': 'Tuesday 6:30', 
     'social_time': '6:30pm'
     },
    {'social_id': 2,
     'venue_id': 1, 
     'social_name': 'Tuesday 8:30', 
     'social_time': '8:30pm'
     },
]

for social in socials:
    pass