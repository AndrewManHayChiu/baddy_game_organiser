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
        self.queue = []
        
    def add_player(self, player):
        self.players.append(player)
        self.queue.append(player.name)
    
    def remove_player(self, player_name):
        if player_name in self.queue:
            self.queue.remove(player_name)
            print(player_name, "has been removed from the queue.")
        else:
            print('Player not in the queue.')
    
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
        for count, player in enumerate(self.players, start=1):
            print('    ', count, player.name, '(' + str(player.tier) +')')
        print()
        
        print('Queue:')
        print(self.queue)
        print()
        
        print('Games:')