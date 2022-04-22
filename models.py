from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

connection_string = 'sqlite:///test2.db'

Base = declarative_base()

engine = create_engine(connection_string, echo=True)

Session = sessionmaker()


# Using sqlalchemy, Python classes can be directly added to the database
class Player(Base):
    __tablename__ = "players"
    player_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    gender = Column(String, nullable=True)
    # games = relationship("Games", backref=backref("players"))
    
    def __repr__(self):
        return f"<Player name={self.name}>"
    
# ac = Player(player_id=1, name='Andrew Chiu', gender='male')
# print(ac)

class Games(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.player_id"))
    game_type = Column(String)
    win = Column(Integer)
    played_date = Column(DateTime, default=datetime.utcnow)

class Player_tiers(Base):
    __tablename__ = "player_tiers"
    player_id = Column(Integer, ForeignKey("players.player_id"), primary_key=True)
    tier = Column(Integer)
    updated_at_date = Column(DateTime, default=datetime.utcnow)

player_games = Table(
        "player_games",
        Base.metadata,
        Column("player_id", Integer, ForeignKey("players.player_id")),
        Column("game_id", Integer, ForeignKey("games.game_id")),
    )