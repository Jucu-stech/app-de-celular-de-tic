from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

class SexoVaca(enum.Enum):
    MACHO = "macho"
    HEMBRA = "hembra"

class CategoriaVaca(enum.Enum):
    TERNERO = "ternero"
    NOVILLO = "novillo"
    TORO = "toro"
    VACA = "vaca"
    VACONA = "vacona"

class Vaca(Base):
    __tablename__ = "vacas"

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, unique=True, index=True)  # Número de caravana o chip
    nombre = Column(String, nullable=True)
    fecha_nacimiento = Column(Date)
    sexo = Column(Enum(SexoVaca))
    categoria = Column(Enum(CategoriaVaca))
    raza = Column(String)
    padre = Column(String, nullable=True)
    madre = Column(String, nullable=True)
    propietario_nombre = Column(String)
    propietario_telefono = Column(String)
    propietario_direccion = Column(String)
    observaciones = Column(String, nullable=True)

class Vacuna(Base):
    __tablename__ = "vacunas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    dosis_requeridas = Column(Integer)
    periodicidad = Column(Integer)  # Cada cuántos meses se debe aplicar
    edad_minima = Column(Integer)  # Edad mínima en meses para aplicar
    observaciones = Column(String, nullable=True)

class RegistroVacunacion(Base):
    __tablename__ = "registros_vacunacion"

    id = Column(Integer, primary_key=True, index=True)
    vaca_id = Column(Integer, ForeignKey("vacas.id"))
    vacuna_id = Column(Integer, ForeignKey("vacunas.id"))
    fecha_aplicacion = Column(Date)
    dosis_numero = Column(Integer)
    lote = Column(String)
    veterinario = Column(String)
    proxima_dosis = Column(Date)  # Fecha estimada para la próxima dosis
    peso = Column(Integer, nullable=True)  # Peso del animal al momento de la vacunación
    observaciones = Column(String, nullable=True)

    vaca = relationship("Vaca")
    vacuna = relationship("Vacuna") 