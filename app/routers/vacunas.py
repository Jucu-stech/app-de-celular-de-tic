from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, auth
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Vacuna)
def create_vacuna(
    vacuna: schemas.VacunaCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    return crud.create_vacuna(db=db, vacuna=vacuna)

@router.get("/", response_model=List[schemas.Vacuna])
def read_vacunas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    vacunas = crud.get_vacunas(db, skip=skip, limit=limit)
    return vacunas

@router.get("/{vacuna_id}", response_model=schemas.Vacuna)
def read_vacuna(
    vacuna_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_vacuna = crud.get_vacuna(db, vacuna_id=vacuna_id)
    if db_vacuna is None:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    return db_vacuna 