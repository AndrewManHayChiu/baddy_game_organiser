import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

database = 'sqlite:///test.db'

def extract_player(player_id):
    engine = create_engine(database, echo=False)
    conn = engine.connect()

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

def create_player():
    engine = create_engine(database, echo=False)
    conn = engine.connect()

    print("Enter new player's name")
    name = input()
    
    # Check if player's name already exists in the database

    print("Is the player male, female or prefer not to say? (male/female/undefined)")
    gender = input()
    
    print("Enter player's skill level (4 - 9):")
    tier = input()
    
    # Save new player info to database
    new_data = (None, name, gender)
    q = text("INSERT INTO players VALUES (?, ?, ?)")
    try:
        conn.execute(q, new_data)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    
class Player:
    """a player"""
    
    def __init__(self, player_id):
        player_data = extract_player(player_id=player_id)
        self.id = player_id
        self.name = player_data[1]
        self.gender = player_data[2]
        self.tier = player_data[3]
        
