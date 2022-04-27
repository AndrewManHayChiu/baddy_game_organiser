import pandas as pd

# Migrate classes to sqlalchemy ORM classes

# TODO: Implementing players and queues from Session to fit in with sqlalchemy
#

class Session:
    """a baddy session"""
    
    def __init__(self, weekday, session):
        # self.weekday = weekday
        self.session = session
        self.players = []
        self.games = pd.DataFrame({'type': [], 'players': []})
        self.courts = 6
        # self.doubles = True
        self.points = 21
        # self.floor_type = 'wood'
        # self.skill_levels = 'open'
        # self.venue = 'dtba'
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
    
    def add_game(self, players=[]):
        if len(players) == 0: # no players are supplied; auto allocation
            game = Game(queue=self.queue)
        elif len(players) == 4: # if all 4 players are manually supplied
            game = Game(queue=self.queue, players=players)
                     
        self.games = pd.concat([self.games,
                                pd.DataFrame({
                                    'type': [game.game_type], 
                                    'players': [game.players]})])
        
        # Move players to the back of the queue
        for player in game.players:
            self.queue.remove(player)
            self.queue.append(player)
    
    def info(self, verbose=False):
        print('SESSION INFO:')
        if verbose == True:
            print('    Venue:', self.venue)
            print('    Time:', self.weekday, self.session)
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
        
        print('Games played:', len(self.games))
        print()
        
        print('Queue:')
        print(self.queue)


class Game:
    """
        A baddy game
        By default, MD, and automatic allocation from Session.queue
        
        game_types:
            - MD: Men's Doubles
            - WD: Women's Doubles
            - XD: Mixed Doubles
    """
    
    def __init__(self, queue, players=[]):
        self.doubles = True
        self.game_type = "MD"

        if len(players)  == 0: # no players are supplied; auto allocation
            self.players = queue[0:4]
        elif len(players) == 4: # if all 4 players are manually supplied
            self.players = players
    
    def info(self):
        print('GAME INFO')
        print('Type:', self.game_type)
        print('Players:')
        for count, player in enumerate(self.players, start=1):
            print('    ', count, player)
