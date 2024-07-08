#!/usr/bin/python3

"""
    A script that adds a new state to a State class.
    It also returns all states in the table
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    argv = sys.argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
            f'mysql+mysqldb://:{username}:{password}@localhost:3306/{database}'
            )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    # Add a new state
    add_state = 'Louisiana'
    new_state = State(name=add_state)
    session.add(new_state)

    results = session.query(State).filter_by(name=add_state)first()
    print(f"{results.id}")
