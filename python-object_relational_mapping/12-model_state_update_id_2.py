#!/usr/bin/python3
"""
This module updates a record in the 'states' table of a database
using SQLAlchemy ORM.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLAlchemy base class
Base = declarative_base()

# Define the States table
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

# Connect to the database
engine = create_engine('sqlite:///states.db')  # Change this to your DB
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def update_state(state_id, new_name):
    """
    Updates the name of a state with a given id.
    Prints 'No record found' if id does not exist.
    """
    state = session.query(State).filter_by(id=state_id).first()
    if state:
        state.name = new_name
        session.commit()
        print(f"Record {state_id} updated to {new_name}")
    else:
        print("No record found")

# Example usage (for testing)
if __

