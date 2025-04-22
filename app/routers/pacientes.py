from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, auth
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Paciente)
def create_paciente(
    paciente: schemas.PacienteCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_paciente = crud.get_paciente_by_dni(db, dni=paciente.dni)
    if db_paciente:
        raise HTTPException(status_code=400, detail="DNI ya registrado")
    return crud.create_paciente(db=db, paciente=paciente)

@router.get("/", response_model=List[schemas.Paciente])
def read_pacientes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    pacientes = crud.get_pacientes(db, skip=skip, limit=limit)
    return pacientes

@router.get("/{paciente_id}", response_model=schemas.Paciente)
def read_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_paciente = crud.get_paciente(db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente 