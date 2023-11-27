#!/usr/bin/python3
"""Print the id of the state passed as an arg
"""


from model_state import Base, State
from sqlalchemy import (create_engine)
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    state_name = sys.argv[4]
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Mysession = Session()

    states = Mysession.query(State).filter(State.name == state_name).first()

    if states:
        print("{}".format(states.id))
    else:
        print("Not found")

    Mysession.close()
