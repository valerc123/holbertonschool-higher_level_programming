#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create conection to engine of db
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create metadata
    Base.metadata.create_all(engine)
    # Create instance for engine
    Session = sessionmaker(bind=engine)
    # initialize
    session = Session()
    # create query
    query = session.query(State)
    # order date
    colum = query.filter(State.name.like('%a%')).order_by(State.id)

    for row in colum:
        print("{}: {}".format(row.id, row.name))
