#!/usr/bin/python3
"""
This script prints the State object matching the name
passed as the 4th argument into the program
from database passed into program

Using SQLalchemy, this script connects to a MySQL server running on
localhost at port 3306.

This script takes 4 arguments: mysql username,
mysql password, database name, and state name.

The first three arguments are used to connect to the MySQL server.
The fourth argument is used to print the right state id.
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

    state = session.query(State) \
        .filter(State.name == sys.argv[4]) \
        .first()

    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))
