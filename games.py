
class Game:
    """a baddy game"""
    
    game_types = ["mens", "womens", "mixed"]
    
    def __init__(self):
        self.players = []
        self.doubles = True
        self.game_type = "mens"
        self.team_1 = []
        self.team_2 = []
        self.team_1_score = 21 # team 1 wins by default; can override this value
        self.team_2_score = ''

test_game = Game()
test_game.team_1
test_game.team_1_score
test_game.team_1_score = 22
test_game.team_1_score