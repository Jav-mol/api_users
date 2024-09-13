from fastapi import FastAPI
from schemas.users import User
from core.config import setting

from db.mongodb.db import get_db_mongo
#from db.psql.db import get_db_psql 
from services.users import insert_user


from pymongo import client_session 

connection = get_db_mongo()
user1 = User(username="Javier3", hashed_password="1234", email="javi@gmail.com", rule="admin")

print(insert_user(db=connection, user=user1))

#print(user1.model_dump())
#resul = connection.insert_one(user1.model_dump())
#resul.inserted_id

col = connection.find()

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