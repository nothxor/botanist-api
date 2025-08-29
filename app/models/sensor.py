from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index = True)
    plant_id = Column(Integer, ForeignKey("plants.id"), nullable=False)

    sensor_type = Column(String, nullable=False)
    
    raw_value = Column(Float, nullable=True)
    calibration_dry = Column(Float, nullable=True)
    calibration_wet = Column(Float, nullable=True)
    current_value = Column(Float, nullable=True)
    target_value = Column(Float, nullable=True)

    last_updated = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Sensor(id={self.id}, plant.id={self.plant_id}, type={self.sensor_type})>"