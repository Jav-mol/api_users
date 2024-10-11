from utils.security import get_hashed_password, verify_hashed_password

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
    