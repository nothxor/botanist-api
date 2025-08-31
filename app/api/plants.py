from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.plant import Plant

router = APIRouter()

@router.get("/plants")
def get_all_plants(db: Session = Depends(get_db)):
    plants = db.query(Plant).all
    return plants

