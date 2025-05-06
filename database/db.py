from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

engine = create_engine('sqlite:///data/vehicles.db', echo=False)
SessionLocal = sessionmaker(bind=engine)

def create_bank():
    Base.metadata.create_all(bind=engine)
