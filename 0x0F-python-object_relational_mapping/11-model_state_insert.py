#!/usr/bin/python3
"""
This script adds the State object "Louisiana"
to the database passed to the program and
prints the id of the new State object.

Using SQLalchemy, this script connects to a MySQL server running on
localhost at port 3306.

This script takes 3 arguments: mysql username,
mysql password, and database name.
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

    louisiana = State(name="Louisiana")

    session.add(louisiana)
    session.commit()

    print("{}".format(louisiana.id))
