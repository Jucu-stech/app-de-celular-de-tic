from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import pacientes, vacunas, registros, auth

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="VacunApp API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/auth", tags=["autenticación"])
app.include_router(pacientes.router, prefix="/pacientes", tags=["pacientes"])
app.include_router(vacunas.router, prefix="/vacunas", tags=["vacunas"])
app.include_router(registros.router, prefix="/registros", tags=["registros"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de VacunApp"} 