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

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)
    colum = query.filter(State.id == 2).update({"name": ("New Mexico")})
    session.commit()
    session.close()
