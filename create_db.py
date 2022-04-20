import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = 'test.db'
    
    sql_create_players_table = """
        CREATE TABLE IF NOT EXISTS players (
            player_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
    );
    """

    sql_create_games_table = """
        CREATE TABLE IF NOT EXISTS games (
            game_id INTEGER,
            player_id INTEGER,
            game_type TEXT NOT NULL,
            win INTEGER NOT NULL,
            PRIMARY KEY (player_id, game_id),
            FOREIGN KEY (player_id) # foregin keys must be at end of statement
                REFERENCES players (player_id)
                ON DELETE CASCADE ON UPDATE NO ACTION
        );
    """
    
    sql_create_player_tiers_table = """
        CREATE TABLE IF NOT EXISTS player_tiers (
            player_id INTEGER NOT NULL,
            tier INTEGER NOT NULL,
            FOREIGN KEY (player_id) 
                REFERENCES players (player_id)
        );
    """
    
    # Connects if available; creates if not available
    conn = create_connection(database)  
    
    # Create tables
    if conn is not None:
        create_table(conn, sql_create_players_table)
        create_table(conn, sql_create_games_table)
        create_table(conn, sql_create_player_tiers_table)
    else:
        print("Error - cannot create connection to the database.")


if  __name__ == '__main__':
    main()