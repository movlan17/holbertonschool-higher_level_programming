#!/usr/bin/python3
"""
Adds a new State object "Louisiana" to the database hbtn_0e_6_usa
and prints the new state's id.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new state
    print(new_state.id)

    session.close()
