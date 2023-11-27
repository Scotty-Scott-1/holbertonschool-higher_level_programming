#!/usr/bin/python3
"""Print the first state in the database
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

    states = Mysession.query(State).order_by(State.id).first()

    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")

    Mysession.close()
