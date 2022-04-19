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
            id integer PRIMARY KEY,
            name text NOT NULL,
            tier integer NOT NULL
    );
    """

    sql_create_games_table = """
        CREATE TABLE IF NOT EXISTS games (
            id integer PRIMARY KEY,
            type text NOT NULL,
            FOREIGN KEY (player_id) REFERENCES players (id),
            win boolean NOT NULL
        );
    """
    
    conn = create_connection(database)
    
    # Create tables
    if conn is not None:
        create_table(conn, sql_create_players_table)
        create_table(conn, sql_create_games_table)
    else:
        print("Error - cannot create connection to the database.")
    
if  __name__ == '__main__':
    main()