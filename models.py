from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.sql import func
from datetime import datetime

connection_string = 'sqlite:///test2.db'

Base = declarative_base()

engine = create_engine(connection_string, echo=True, future=True)

Session = sessionmaker()

# Using sqlalchemy, Python classes can be directly added to the database

# TODO: Create relationship between Player and PlayerTier tables
class Player(Base):
    __tablename__ = "players"
    
    player_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String, nullable=True)
    
    def __init__(self, player_id, name, gender):
        self.player_id = player_id
        self.name = name
        self.gender = gender
        
    def __repr__(self):
        return f"<Player name: {self.name}>"

class Venue(Base):
    __tablename__ = "venues"
    
    venue_id = Column(Integer, primary_key=True)
    venue_name = Column(String)
    floor_type = Column(String)
    
    def __repr__(self):
        return f"<Venue name: {self.venue_name}>"

class Social(Base):
    __tablename__ = "socials"
    
    social_id = Column(Integer, primary_key=True)
    venue_id = Column(Integer, ForeignKey("venues.venue_id"))
    social_name = Column(String)
    social_weekday = Column(String)
    social_time = Column(String)
    doubles = Column(Integer, default=1)
    social_skill_levels = Column(String, default='open')
    
    def __repr__(self):
        return f"<Social name: {self.social_name}>"

class Game(Base):
    __tablename__ = "games"
    
    game_id = Column(Integer, primary_key=True)
    social_id = Column(Integer, ForeignKey("socials.social_id"))
    player_id = Column(Integer, ForeignKey("players.player_id"))
    game_type = Column(String)
    win = Column(Integer)
    played_date = Column(DateTime(timezone=True), server_default=func.now())

class PlayerTier(Base):
    __tablename__ = "player_tiers"
    
    player_id = Column(Integer, ForeignKey("players.player_id"), primary_key=True)
    tier = Column(Integer)
    updated_at_date = Column(DateTime(timezone=True), server_default=func.now())
    
    