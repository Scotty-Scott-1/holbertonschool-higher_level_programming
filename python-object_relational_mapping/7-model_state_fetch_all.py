#!/usr/bin/python3
"""List all state objects from the database
"""


from model_state import Base, State
from sqlalchemy import (create_engine)
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Mysession = Session()

    states = Mysession.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
