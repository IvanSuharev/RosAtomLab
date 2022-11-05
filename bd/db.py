from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from sqlalchemy.orm import Session, declarative_base, sessionmaker

load_dotenv()
db_link = os.getenv("DB_LINK")

engine = create_engine(db_link)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
