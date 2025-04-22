# VacunApp - Sistema de Gestión de Vacunación

Sistema de gestión de vacunación desarrollado con FastAPI y PostgreSQL.

## Requisitos Previos

- Python 3.8+
- PostgreSQL
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd vacunapp_backend
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos PostgreSQL:
```sql
CREATE DATABASE vacunapp;
CREATE USER vacunapp_user WITH PASSWORD 'tupassword';
GRANT ALL PRIVILEGES ON DATABASE vacunapp TO vacunapp_user;
```

5. Configurar variables de entorno:
   - Copiar el archivo `.env.example` a `.env`
   - Modificar las variables según tu configuración

## Ejecución

1. Iniciar el servidor:
```bash
uvicorn app.main:app --reload
```

2. Acceder a la documentación de la API:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Estructura del Proyecto

```
vacunapp_backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # Configuración principal
│   ├── models.py        # Modelos de base de datos
│   ├── schemas.py       # Esquemas Pydantic
│   ├── crud.py          # Operaciones CRUD
│   ├── database.py      # Configuración DB
│   ├── auth.py          # Autenticación
│   └── routers/         # Endpoints API
│       ├── pacientes.py
│       ├── vacunas.py
│       └── registros.py
├── requirements.txt
└── .env
```

## Endpoints Principales

### Autenticación
- POST /auth/token - Obtener token JWT
- POST /auth/register - Registrar nuevo usuario

### Pacientes
- POST /pacientes/ - Crear nuevo paciente
- GET /pacientes/ - Listar pacientes
- GET /pacientes/{id} - Obtener paciente por ID

### Vacunas
- POST /vacunas/ - Crear nueva vacuna
- GET /vacunas/ - Listar vacunas
- GET /vacunas/{id} - Obtener vacuna por ID

### Registros de Vacunación
- POST /registros/ - Crear nuevo registro
- GET /registros/ - Listar registros
- GET /registros/{id} - Obtener registro por ID

## Seguridad

- Autenticación basada en JWT
- Contraseñas hasheadas con bcrypt
- Protección contra CSRF
- Validación de datos con Pydantic

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 