from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from app.core.database import Base

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    species = Column(String, nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow, nullable=False)
    notes = Column(String, nullable=True)

    def __repr__(self):
        return f"<Plant(id={self.id}, species={self.species})>"