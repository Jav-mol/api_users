from fastapi import FastAPI
from api.routers.users import router as router_users
from api.routers.auth import router as router_auth
from api.routers.books import router as router_books
from api.routers.user import router as router_user

app = FastAPI()

app.include_router(router_users)
app.include_router(router_auth)
app.include_router(router_books)
app.include_router(router_user)


"ctrl + o / enter / ctrl + x"


""" 
app/
│
├── api/                     # Controladores o Routers de FastAPI
│   └── routers/
│       ├── auth.py           # Maneja las solicitudes HTTP para autenticación
│       ├── user.py           # Maneja las solicitudes HTTP para usuarios
│
├── services/                 # Lógica de negocio
│   ├── auth_service.py       # Lógica de autenticación
│   ├── user_service.py       # Lógica de manejo de usuarios
│
├── crud/                     # Operaciones CRUD (interacciones con la DB)
│   ├── user_crud.py          # Funciones CRUD para usuarios
│
├── db/                       # Configuración de bases de datos
│   ├── psql/                 # Conexión y configuración de PostgreSQL
│   ├── mongodb/              # Conexión y configuración de MongoDB
│
├── schemas/                  # Definición de modelos de datos (schemas)
│   ├── auth_schemas.py       # Schemas para autenticación (ej. login, registro)
│   ├── user_schemas.py       # Schemas para manejo de usuarios (ej. creación)
│
├── core/                     # Configuraciones y utilidades del sistema
│   ├── config.py             # Configuraciones generales de la aplicación
│
├── main.py                   # Punto de entrada de la aplicación (FastAPI)
│
└── tests/                    # Carpeta de pruebas unitarias
    ├── __init__.py           # Inicialización de paquete para tests
    ├── api/
    │   ├── test_auth.py      # Pruebas unitarias para el router de autenticación
    │   ├── test_user.py      # Pruebas unitarias para el router de usuarios
    ├── services/
    │   ├── test_auth_service.py   # Pruebas unitarias para auth_service.py
    │   ├── test_user_service.py   # Pruebas unitarias para user_service.py
    ├── crud/
    │   ├── test_user_crud.py      # Pruebas unitarias para user_crud.py
    ├── schemas/
    │   ├── test_auth_schemas.py   # Pruebas unitarias para auth_schemas.py
    │   ├── test_user_schemas.py   # Pruebas unitarias para user_schemas.py
    ├── db/
    │   ├── test_psql.py           # Pruebas unitarias para conexión/configuración de PostgreSQL
    │   ├── test_mongodb.py        # Pruebas unitarias para conexión/configuración de MongoDB
    └── core/
        ├── test_config.py         # Pruebas unitarias para la configuración general

"""

""" 
└── tests/
    ├── unit/                  # Pruebas unitarias
    │   ├── __init__.py
    │   ├── api/
    │   ├── services/
    │   ├── crud/
    │   ├── schemas/
    │   └── core/
    │
    └── integration/            # Pruebas de integración
        ├── __init__.py
        ├── test_api_integration.py    # Pruebas de integración para los endpoints completos
        ├── test_auth_integration.py   # Pruebas de integración para autenticación (ej. login)
        ├── test_user_integration.py   # Pruebas de integración para operaciones de usuarios
        └── test_db_integration.py     # Pruebas de integración con la base de datos
"""
