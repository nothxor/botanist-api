from pydantic import BaseModel

class PlantCreate(BaseModel):
    species: str
    notes: str = None