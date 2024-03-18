#!/usr/bin/python3
""" A class definition of a State"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

metadata_states = MetaData()
Base = declarative_base(metadata=metadata_states)


class State(Base):
    """ id and name attribute for each state """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
