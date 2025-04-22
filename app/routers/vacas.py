from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, auth
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Vaca)
def create_vaca(
    vaca: schemas.VacaCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_vaca = crud.get_vaca_by_identificacion(db, identificacion=vaca.identificacion)
    if db_vaca:
        raise HTTPException(status_code=400, detail="Identificación ya registrada")
    return crud.create_vaca(db=db, vaca=vaca)

@router.get("/", response_model=List[schemas.Vaca])
def read_vacas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    vacas = crud.get_vacas(db, skip=skip, limit=limit)
    return vacas

@router.get("/{vaca_id}", response_model=schemas.Vaca)
def read_vaca(
    vaca_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_vaca = crud.get_vaca(db, vaca_id=vaca_id)
    if db_vaca is None:
        raise HTTPException(status_code=404, detail="Vaca no encontrada")
    return db_vaca 