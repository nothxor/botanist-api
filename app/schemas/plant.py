from typing import Optional
from pydantic import BaseModel, Field

class PlantCreate(BaseModel):
    species: str
    notes: str = None

class PlantUpdate(BaseModel):
    species: Optional[str] = Field(None)
    notes: Optional[str] = Field(None)