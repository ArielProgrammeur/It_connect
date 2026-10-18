from sqlalchemy import create_engine    
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)