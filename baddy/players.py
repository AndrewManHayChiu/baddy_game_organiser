import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///test.db', echo=False)
conn = engine.connect()

def extract_player(player_id, connection=conn):
    t = text("""
                SELECT DISTINCT 
                    players.player_id, 
                    players.name, 
                    players.gender,
                    player_tiers.tier
                FROM players
                LEFT JOIN player_tiers on players.player_id = player_tiers.player_id
                WHERE players.player_id = 
             """ + str(player_id) )
    result = conn.execute(t).fetchall()
    return(result[0])

class Player:
    """a player"""
    
    def __init__(self, player_id):
        player_data = extract_player(player_id=player_id)
        self.id = player_id
        self.name = player_data[1]
        self.gender = player_data[2]
        self.tier = player_data[3]