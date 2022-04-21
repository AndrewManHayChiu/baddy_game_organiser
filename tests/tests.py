import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlalchemy
from sqlalchemy import create_engine

from baddy.sessions import Session
from baddy.players import Player
from baddy.players import extract_player, create_player

engine = create_engine('sqlite:///test.db', echo=False)
conn = engine.connect()

# Extract player from database
player = extract_player(player_id=2)
player.player_id
player.name
player.gender
player.tier

# Create a new player; adds to the database
# TODO: Fix this
# create_player()

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
