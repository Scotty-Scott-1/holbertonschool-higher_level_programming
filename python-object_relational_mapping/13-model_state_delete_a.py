#!/usr/bin/python3
"""Delete all rows in States, where name has an "a"
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

    rows_to_delete = Mysession.query(
        State).filter(State.name.like('%a%')).all()

    for row in rows_to_delete:
        Mysession.delete(row)

    Mysession.commit()
    Mysession.close()
