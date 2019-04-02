#!/usr/bin/python3
"""
This script lists the first State object from database passed into program

Using SQLalchemy, this script connects to a MySQL server running on
localhost at port 3306.

This script takes 3 arguments: mysql username,
mysql password, and database name.
These arguments are used to connect to the MySQL server.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
