from models import Dog

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Dog

# Function to create the table
def create_table(base, engine):
    base.metadata.create_all(engine)

# Function to save a Dog instance
def save(session, dog):
    session.add(dog)
    session.commit()

# Function to get all Dog instances
def get_all(session):
    return session.query(Dog).all()

# Function to find a Dog by name
def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

# Function to find a Dog by ID
def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

# Function to find a Dog by name and breed
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

# Function to update a Dog's breed
def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()
