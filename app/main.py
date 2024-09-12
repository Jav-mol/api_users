from fastapi import FastAPI
from core.config import setting
from db.mongodb.db import get_db_mongo
#from db.psql.db import get_db_psql 

from pymongo import client_session 

connection = get_db_mongo()
col = connection.find()

print(col)

for i in col:
    print(col)


#try:
#    print(type(db.client))
#except Exception as e:
#    print(f"Error: {e}")
#app = FastAPI()
#app.include_router(app1)

""" 
app/
│
├── api/
│   └── routers/
│       ├── auth.py       # Maneja las solicitudes HTTP para autenticación
│       ├── user.py       # Maneja las solicitudes HTTP para usuarios
│
├── services/             # Lógica de negocio
│   ├── auth_service.py   # Lógica de autenticación
│   ├── user_service.py   # Lógica de manejo de usuarios
│
├── crud/                 # Acceso a datos (CRUD)
│   ├── user_crud.py      # Funciones CRUD para usuarios
│
├── db/
│   ├── psql/             # Conexión y configuración de PostgreSQL
│   ├── mongodb/          # Conexión y configuración de MongoDB
│
├── schemas/              # Definición de estructuras de datos
│   ├── auth_schemas.py   # Schemas para autenticación (ej. login, registro)
│   ├── user_schemas.py   # Schemas para manejo de usuarios (ej. creación)
│
├── core/
│   ├── config.py         # Configuraciones generales de la aplicación
│
├── main.py               # Punto de entrada de la API

"""