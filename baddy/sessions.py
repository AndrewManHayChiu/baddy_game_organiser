
class Session:
    """a baddy session"""
    
    def __init__(self, weekday, session):
        self.weekday = weekday
        self.session = session
        self.players = []
        self.games = []
        self.courts = 6
        self.doubles = True
        self.points = 21
        self.floor_type = 'wood'
        self.skill_levels = 'open'
        self.venue = 'dtba'
        
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            print('Player not in this session.')
    
    def add_game(self, game):
        self.games.append(game)
        
    def info(self, verbose=False):
        print('Session:', self.weekday, self.session)
        if verbose == True:
            print('    Venue:', self.venue)
            print('    Courts:', self.courts)
            print('    Floor type:', self.floor_type)
            print('    Points:', self.points)
            print('    Doubles:', self.doubles)
            print('    Skill levels:', self.skill_levels)
        print()
        print('Players:')
        for player in self.players:
            print('    ', player.name)
        print()
        print('Games:')
        