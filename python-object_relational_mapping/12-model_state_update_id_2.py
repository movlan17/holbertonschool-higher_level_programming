#!/usr/bin/python3
"""
Module to update a state record in a database using SQLAlchemy ORM.

This module:
- Defines a State class mapped to the 'states' table
- Updates a state's name by its ID
- Handles cases where the record does not exist
- Includes sample test cases for validation
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Base class for ORM
Base = declarative_base()

# State class mapped to 'states' table
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

# Create SQLite database connection
engine = create_engine('sqlite:///states.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def update_state(state_id, new_name):
    """
    Update the name of a state by ID.
    Prints 'No record found' if the state ID does not exist.
    """
    state = session.query(State).filter_by(id=state_id).first()
    if state:
        state.name = new_name
        session.commit()
        print(f"Record {state_id} updated to {new_name}")
    else:
        print("No record found")

# --- Test setup ---
def setup_initial_records():
    """Add initial records if table is empty"""
    if session.query(State).count() == 0:
        session.add_all([
            State(name="California"),
            State(name="Texas"),
            State(name="New York"),
            State(name="Florida")
        ])
        session.commit()

# --- Test cases ---
if __name__ == "__main__":
    setup_initial_records()
    
    print("Case: 4 initial records")
    update_state(2, "Arizona")  # Existing record

    print("Case: No record")
    update_state(10, "Nevada")  # Non-existing record

    print("Case: Many records")
    update_state(1, "Washington")  # Another existing record

session.close()

