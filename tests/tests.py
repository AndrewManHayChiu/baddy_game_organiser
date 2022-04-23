import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlalchemy
from sqlalchemy import create_engine

from models import Player, PlayerTiers, Session, engine
from baddy.players import create_player, update_player_tier, extract_player

session = Session(bind=engine)

# Create, update and extract player data from database
create_player(player_id=10, name='test', gender='female', tier=8)
update_player_tier(player_id=1, tier=7)
player = extract_player(player_id=1)
player.player_id
player.name
player.gender


# Create a new session and add players to session
test_session = Session(weekday='Tuesday', session='6:30')

# Add players using Player id
test_session.add_player(Player(player_id=1))
test_session.add_player(Player(player_id=2))
test_session.add_player(Player(player_id=3))
test_session.add_player(Player(player_id=4))
test_session.add_player(Player(player_id=5))
test_session.add_player(Player(player_id=6))

# Print session information
test_session.info(verbose=True)

# Games can be created automatically
test_session.add_game()
test_session.games

# And players are moved to the back of the Queue
test_session.info(verbose=True)

# Games can be also be created manually
test_session.add_game(players=['David Yeung', 'Andrew', 'Felix', 'Terence'])
test_session.info(verbose=True)

# Player leaves; remove from queue
test_session.remove_player(player_name='David Ng')
test_session.info(verbose=True)
