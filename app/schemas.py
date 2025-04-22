from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from .models import SexoVaca, CategoriaVaca

class UsuarioBase(BaseModel):
    email: EmailStr
    nombre: str
    apellido: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    es_admin: bool

    class Config:
        from_attributes = True

class VacaBase(BaseModel):
    identificacion: str
    nombre: Optional[str] = None
    fecha_nacimiento: date
    sexo: SexoVaca
    categoria: CategoriaVaca
    raza: str
    padre: Optional[str] = None
    madre: Optional[str] = None
    propietario_nombre: str
    propietario_telefono: str
    propietario_direccion: str
    observaciones: Optional[str] = None

class VacaCreate(VacaBase):
    pass

class Vaca(VacaBase):
    id: int

    class Config:
        from_attributes = True

class VacunaBase(BaseModel):
    nombre: str
    descripcion: str
    dosis_requeridas: int
    periodicidad: int  # En meses
    edad_minima: int  # Edad mínima en meses
    observaciones: Optional[str] = None

class VacunaCreate(VacunaBase):
    pass

class Vacuna(VacunaBase):
    id: int

    class Config:
        from_attributes = True

class RegistroVacunacionBase(BaseModel):
    vaca_id: int
    vacuna_id: int
    fecha_aplicacion: date
    dosis_numero: int
    lote: str
    veterinario: str
    proxima_dosis: date
    peso: Optional[int] = None
    observaciones: Optional[str] = None

class RegistroVacunacionCreate(RegistroVacunacionBase):
    pass

class RegistroVacunacion(RegistroVacunacionBase):
    id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None 