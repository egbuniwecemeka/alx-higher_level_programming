#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    argv = sys.argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).filter_by(name=state_name).all()
    for result in results:
        print(f"{result.id}")
