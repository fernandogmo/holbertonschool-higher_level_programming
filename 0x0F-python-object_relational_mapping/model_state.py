#!/usr/bin/python3
"""
The `State` class inherits from `Base`, an SQLAlchemy declarative base.
Instances of `State` will be a MySQL database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    This class is linked to the states table.
    Attributes:
        id: Integer, required, primary key
        name: String, required
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
