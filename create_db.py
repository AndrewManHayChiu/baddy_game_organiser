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

def insert_data(conn, insert_data_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(insert_data_sql)
        conn.commit()
        cursor.close()
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
            FOREIGN KEY (player_id) 
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
    
    sql_insert_player_data = """
        INSERT INTO players (player_id, name)
        VALUES
            (1, 'Andrew'), 
            (2, 'Felix'), 
            (3, 'Billy'), 
            (4, 'Terence'), 
            (5, 'David')
    """
    
    sql_insert_tier_data = """
        INSERT INTO player_tiers (player_id, tier)
        VALUES
            (1, 8),
            (2, 8),
            (3, 8),
            (4, 8),
            (5, 7)
    """
    
    conn = create_connection(database)  
    
    # Create tables
    if conn is not None:
        create_table(conn, sql_create_players_table)
        create_table(conn, sql_create_games_table)
        create_table(conn, sql_create_player_tiers_table)
    else:
        print("Error - cannot create connection to database.")

    # Add data
    if conn is not None:
        insert_data(conn, sql_insert_player_data)
        insert_data(conn, sql_insert_tier_data)
    else:
        print("Error - cannot create connection to database.")

if  __name__ == '__main__':
    main()