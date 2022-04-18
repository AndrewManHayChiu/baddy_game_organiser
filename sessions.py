

class Session:
    "a baddy session"
    
    def __init__(self, weekday, session):
        self.weekday = weekday
        self.session = session
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            print('Player not in this session.')
        
# Tests
test_session = Session(weekday='Tuesday', session='6:30')
test_session.weekday

test_session.players
test_session.add_player('Felix')
test_session.add_player('Andrew')
test_session.players

test_session.remove_player('Andrew')
test_session.players