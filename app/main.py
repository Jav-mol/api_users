from fastapi import FastAPI
from schemas.users import UserCreate, UserBD
from core.config import setting

#from db.mongodb.db import get_db_mongo
from db.psql import get_db 
#from services.users import insert_user


#connection = get_db_mongo()
user1 = UserCreate(username="Javier3", password="1234", email="javi@gmail.com")

#user_dict = user1.model_dump()

user2 = UserBD(**user1.model_dump())

#print(user2)
#print(insert_user(db=connection, user=user1))

#print(user1.model_dump())
#resul = connection.insert_one(user1.model_dump())
#resul.inserted_id

#col = connection.find()

#print(col)

#for i in col:
#    print(i)


#try:
#    print(type(db.client))
#except Exception as e:
#    print(f"Error: {e}")
#app = FastAPI()
#app.include_router(app1)

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