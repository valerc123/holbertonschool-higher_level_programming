#!/usr/bin/python3
"""
    Script that prints all City objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create conection to engine of db
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create metadata
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City)
    relation = query.filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in relation:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
