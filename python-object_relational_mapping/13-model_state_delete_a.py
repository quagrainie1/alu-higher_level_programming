#!/usr/bin/python3
"""Script that deletes all States with a name containing 'a'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(State).filter(
        State.name.contains('a')
    ).delete(synchronize_session=False)
    session.commit()
    session.close()
