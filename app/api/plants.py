from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.models.plant import Plant
from app.schemas.plant import PlantCreate

router = APIRouter()

@router.get("/plants")
def get_all_plants(db: Session = Depends(get_db)):
    plants = db.query(Plant).all()
    return plants

@router.get("/plants/{id}")
def get_single_plant(id: int, db: Session = Depends(get_db)):
    return get_plant_or_404(id, db)

@router.delete("/plants/{id}")
def delete_single_plant(id: int, db: Session = Depends(get_db)):
    plant = get_plant_or_404(id, db)
    db.delete(plant)
    db.commit()
    return plant
        
@router.post("/plants")
def create_new_plant(plant: PlantCreate, db: Session = Depends(get_db)):
    new_plant = Plant(species=plant.species, notes=plant.notes)
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return new_plant

def get_plant_or_404(plant_id: int, db: Session):
    plant = db.query(Plant).filter(Plant.id == plant_id).first()
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return plant
