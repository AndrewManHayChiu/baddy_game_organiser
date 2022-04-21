from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

player_games = Table(
        "player_games",
        Base.metadata,
        Column("player_id", Integer, ForeignKey("players.player_id")),
        Column("game_id", Integer, ForeignKey("games.game_id")),
    )

class Games(Base):
        __tablename__ = "games"
        game_id = Column(Integer, primary_key=True)
        player_id = Column(Integer, ForeignKey("player_id"))
        game_type = Column(String)
    
    class Players(Base):
        __tablename__ = "players"
        player_id = Column(Integer, primary_key=True)
        name = Column(String)
        gender = Column(String)
        games = relationship("Games", backref=backref("players"))
    
    class Player_tiers(Base):
        __tablename__ = "player_tiers"
        player_id = Column(Integer, ForeignKey("players.player_id"))
        tier = Column(Integer)