from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.models.plant import Plant
from app.schemas.plant import PlantCreate

router = APIRouter()

@router.get("/plants")
def get_all_plants(db: Session = Depends(get_db)):
    plants = db.query(Plant).all()
    return plants

@router.post("/plants")
def create_new_plant(plant: PlantCreate, db: Session = Depends(get_db)):
    new_plant = Plant(species=plant.species, notes=plant.notes)
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return new_plant
