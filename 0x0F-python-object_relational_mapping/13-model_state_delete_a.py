#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter 'a'
from the database passed into the program

Using SQLalchemy, this script connects to a MySQL server running on
localhost at port 3306.

This script takes 3 arguments: mysql username,
mysql password, and database name.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State) \
        .filter(State.name.ilike('%a%')) \
        .delete(synchronize_session=False)

    session.commit()
