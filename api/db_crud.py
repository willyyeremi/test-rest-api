from sqlalchemy.orm import Session

from db_connection import session
from db_object import ms_game_title


def get_ms_game_title(connection_session: Session, limit: int, offset: int, **kwargs):
    if kwargs.items():
        return connection_session.query(ms_game_title).filter_by(**kwargs).limit(limit).offset(offset)
    else:
        return connection_session.query(ms_game_title).limit(limit).offset(offset)


if __name__ == "__main__":
    print(get_ms_game_title(connection_session = session, limit = 1, offset = 5, id = 1))
    print(get_ms_game_title(connection_session = session, limit = 1, offset = 5))