from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, func

# Replace 'DATABASE_URL' with your actual PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# SQLAlchemy database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
