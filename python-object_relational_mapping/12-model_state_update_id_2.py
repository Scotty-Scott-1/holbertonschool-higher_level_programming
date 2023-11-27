#!/usr/bin/python3
"""Updated States table. Where id = 2 to New Mexico
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

    row_to_update = Mysession.query(State).filter_by(id=2).first()

    if row_to_update:
        row_to_update.name = "New Mexico"
        Mysession.commit()

    Mysession.close()
