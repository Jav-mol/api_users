from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers.auth import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_login_access():
    response = client.post("login", json={"username":"Javi", "password":"1234"})
    
    print(response)