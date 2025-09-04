from typing import Optional
from pydantic import BaseModel

class PlantCreate(BaseModel):
    species: str
    notes: str = None

class PlantUpdate(BaseModel):
    species: Optional[str] = None
    notes: Optional[str] = None