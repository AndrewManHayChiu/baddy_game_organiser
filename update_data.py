from models import Player, Session, engine

session = Session(bind=engine)

player_update = session.query(Player).filter(Player.name == 'David Ng').first()

player_update.name = 'Ng'

session.commit()