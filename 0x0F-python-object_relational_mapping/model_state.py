#!/usr/bin/python3
""" A class definition of a State"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory:', echo='True')
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql://root:Cemeka1995.@localhost:3306/\
                       hbtn_0e_0_usa', echo=True)
Base.metadata.create_all(engine)
