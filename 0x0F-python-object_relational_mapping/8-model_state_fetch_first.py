#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """

import sys
from sqlalchemy import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.meetadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        return
    else:
        print(instance.id, instance.name, sep=": ")

