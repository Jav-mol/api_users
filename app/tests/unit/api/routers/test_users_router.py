from fastapi.testclient import TestClient

from api.routers.users import router

client = TestClient(router)

def test_create_user():
    response = client.post("/users")
    
    print(response.json())