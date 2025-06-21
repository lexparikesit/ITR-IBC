from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, String
from config import Config

Base = declarative_base()

# URL from .env file
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models inline with Database
class User(Base):
    __tablename__ = 'fact_UserIBC'
    email = Column(String, primary_key=True, index=True)
    password = Column(String)
    name = Column(String)

def get_db():
    db = SessionLocal()

    try:
        yield db
    
    finally:
        db.close()