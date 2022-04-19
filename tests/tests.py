import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from baddy.sessions import Session
from baddy.games import Game
from baddy.players import Player

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

# players
test_player = Player(name='Andrew')
test_player.name
test_player.tier
test_player.tier = 'shit'
test_player.tier

# Create a new session and add players to session
test_session = Session(weekday='Tuesday', session='6:30')

# Players are created when they sign in.
andrew = Player(name='Andrew')
test_session.add_player(andrew)
felix = Player(name='Felix')
test_session.add_player(felix)

# Can access player details
test_session.players[0].name
test_session.players[0].tier

# Games can be created
test_session.add_game(test_game)
test_session.games[0]