from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class ms_game_title(Base):
    __tablename__ = "ms_game_title"
    __table_args__ = {'schema': 'public'}
    id = Column(Integer, primary_key = True)
    game_title = Column(String)
    is_active = Column(Integer)
    create_timestamp = Column(DateTime)
    update_timestamp = Column(DateTime)