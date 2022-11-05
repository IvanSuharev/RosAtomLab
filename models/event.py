from sqlalchemy import Table, Integer, Text, Column, DateTime, String
from bd.db import Base
import datetime


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(String)

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    planned_at = Column(DateTime, nullable=False)