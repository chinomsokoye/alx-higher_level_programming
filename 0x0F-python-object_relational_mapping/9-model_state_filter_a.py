#!/usr/bin/python3
"""
List all state objects that contains the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # create database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query python in database
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))
    session.close()
