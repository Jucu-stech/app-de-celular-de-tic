from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, auth
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.RegistroVacunacion)
def create_registro_vacunacion(
    registro: schemas.RegistroVacunacionCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    # Verificar que el paciente existe
    paciente = crud.get_paciente(db, registro.paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    # Verificar que la vacuna existe
    vacuna = crud.get_vacuna(db, registro.vacuna_id)
    if not vacuna:
        raise HTTPException(status_code=404, detail="Vacuna no encontrada")
    
    # Verificar que el número de dosis es válido
    if registro.dosis_numero > vacuna.dosis_requeridas:
        raise HTTPException(
            status_code=400,
            detail=f"El número de dosis ({registro.dosis_numero}) excede el requerido ({vacuna.dosis_requeridas})"
        )
    
    return crud.create_registro_vacunacion(db=db, registro=registro)

@router.get("/", response_model=List[schemas.RegistroVacunacion])
def read_registros_vacunacion(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    registros = crud.get_registros_vacunacion(db, skip=skip, limit=limit)
    return registros

@router.get("/{registro_id}", response_model=schemas.RegistroVacunacion)
def read_registro_vacunacion(
    registro_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(auth.get_current_user)
):
    db_registro = crud.get_registro_vacunacion(db, registro_id=registro_id)
    if db_registro is None:
        raise HTTPException(status_code=404, detail="Registro de vacunación no encontrado")
    return db_registro 