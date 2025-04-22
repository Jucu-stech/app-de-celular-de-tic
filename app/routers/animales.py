from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, auth
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Animal)
def create_animal(
    animal: schemas.AnimalCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_animal = crud.get_animal_by_identificacion(db, identificacion=animal.identificacion)
    if db_animal:
        raise HTTPException(status_code=400, detail="Identificación ya registrada")
    return crud.create_animal(db=db, animal=animal)

@router.get("/", response_model=List[schemas.Animal])
def read_animales(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    animales = crud.get_animales(db, skip=skip, limit=limit)
    return animales

@router.get("/{animal_id}", response_model=schemas.Animal)
def read_animal(
    animal_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_animal = crud.get_animal(db, animal_id=animal_id)
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return db_animal 