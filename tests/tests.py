import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baddy.sessions import Session
from baddy.sessions import extract_player
from baddy.games import Game
from baddy.players import Player

import sqlite3

# sessions
test_session = Session(weekday='Tuesday', session='6:30')
test_session.weekday

test_session.players
test_session.add_player('Felix')
test_session.add_player('Andrew')
test_session.players

test_session.remove_player('Andrew')
test_session.players
test_session.remove_player('Andrew')
test_session.players

# games
test_game = Game()
test_game.team_1
test_game.team_1_score
test_game.team_1_score = 22
test_game.team_1_score
test_game.team_2_score

# Extract player from database
player = Player(player_id=1)
player.id
player.name
player.tier

# Create a new session and add players to session
test_session = Session(weekday='Tuesday', session='6:30')
test_session.info(verbose=True)

# Add players using Player id
test_session.add_player(Player(player_id=1))
test_session.add_player(Player(player_id=2))
test_session.add_player(Player(player_id=3))
test_session.add_player(Player(player_id=4))
test_session.add_player(Player(player_id=5))

# Can access player details
# test_session.players[0].name
# test_session.players[0].tier
# test_session.players[1].name
# test_session.players[1].tier

# Print session information
test_session.info()
test_session.info(verbose=True)

# Games can be created
test_session.add_game(test_game)
test_session.games[0]

