from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash
from datetime import date, timedelta

# Operaciones CRUD para Usuarios
def get_usuario(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = models.Usuario(
        email=usuario.email,
        hashed_password=hashed_password,
        nombre=usuario.nombre,
        apellido=usuario.apellido
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Operaciones CRUD para Animales
def get_animal(db: Session, animal_id: int):
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()

def get_animal_by_identificacion(db: Session, identificacion: str):
    return db.query(models.Animal).filter(models.Animal.identificacion == identificacion).first()

def get_animales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Animal).offset(skip).limit(limit).all()

def create_animal(db: Session, animal: schemas.AnimalCreate):
    db_animal = models.Animal(**animal.model_dump())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

# Operaciones CRUD para Vacas
def get_vaca(db: Session, vaca_id: int):
    return db.query(models.Vaca).filter(models.Vaca.id == vaca_id).first()

def get_vaca_by_identificacion(db: Session, identificacion: str):
    return db.query(models.Vaca).filter(models.Vaca.identificacion == identificacion).first()

def get_vacas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vaca).offset(skip).limit(limit).all()

def create_vaca(db: Session, vaca: schemas.VacaCreate):
    db_vaca = models.Vaca(**vaca.model_dump())
    db.add(db_vaca)
    db.commit()
    db.refresh(db_vaca)
    return db_vaca

# Operaciones CRUD para Vacunas
def get_vacuna(db: Session, vacuna_id: int):
    return db.query(models.Vacuna).filter(models.Vacuna.id == vacuna_id).first()

def get_vacunas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vacuna).offset(skip).limit(limit).all()

def create_vacuna(db: Session, vacuna: schemas.VacunaCreate):
    db_vacuna = models.Vacuna(**vacuna.model_dump())
    db.add(db_vacuna)
    db.commit()
    db.refresh(db_vacuna)
    return db_vacuna

# Operaciones CRUD para Registros de Vacunación
def get_registro_vacunacion(db: Session, registro_id: int):
    return db.query(models.RegistroVacunacion).filter(models.RegistroVacunacion.id == registro_id).first()

def get_registros_vacunacion(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RegistroVacunacion).offset(skip).limit(limit).all()

def create_registro_vacunacion(db: Session, registro: schemas.RegistroVacunacionCreate):
    # Verificar edad mínima de la vacuna
    vaca = get_vaca(db, registro.vaca_id)
    vacuna = get_vacuna(db, registro.vacuna_id)
    
    edad_vaca = (date.today() - vaca.fecha_nacimiento).days // 30  # Edad en meses
    if edad_vaca < vacuna.edad_minima:
        raise ValueError(f"La vaca es demasiado joven para esta vacuna. Edad mínima requerida: {vacuna.edad_minima} meses")
    
    db_registro = models.RegistroVacunacion(**registro.model_dump())
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro 