from utils.security import get_hashed_password, verify_hashed_password, get_current_user, get_access_token, decode_token

"""
def get_current_user_override():
    data = {"sub":"Javier", "role":"admin"}
    access_token = get_access_token(data=data)
    
    token = Token(access_token=access_token)
    user = get_current_user(token)
    
    return user
"""


def test_get_hashed_password():
    password = "1234"
    hashed_password = get_hashed_password(password)
    
    assert isinstance(hashed_password, str) == True
    assert len(hashed_password) == 60


def test_verify_hashed_password_success():
    hashed_password = get_hashed_password("password")
    password = verify_hashed_password(hashed_password, "password")
    
    assert password == True


def test_verify_hashed_password_fail():
    hashed_password = get_hashed_password("password")
    password = verify_hashed_password(hashed_password, "password1")
    
    assert password == False


def test_get_access_token():
    data = {"sub":"Javier", "role":"admin", "id":1}
    token = get_access_token(data)
    user = decode_token(token)
    
    assert user["sub"] == data["sub"]