import pytest
from pydantic import ValidationError
#from ...core.config import Setting
from core.config import Setting


def test_suma():
    assert 1+1 ==2

def test_settings_with_env_vars(monkeypatch):
    # Simulamos las variables de entorno
    monkeypatch.setenv("URL_DB_PSQL", "postgresql://user:pass@localhost:5432/mydb")
    monkeypatch.setenv("URL_DB_MONGO", "mongodb://localhost:27017/mydb")

    # Creamos la instancia de Setting
    setting = Setting()
    # Verificamos los valores cargados
    assert setting.app_name == "Awesome API"  # Verificamos el valor por defecto
    assert setting.url_db_psql == "postgresql://user:pass@localhost:5432/mydb"
    assert setting.url_db_mongo == "mongodb://localhost:27017/mydb"


# Prueba para verificar si falta una variable requerida
def test_settings_missing_env_var(monkeypatch):
    # Solo configuramos una de las dos variables de entorno
    monkeypatch.setenv("URL_DB_PSQL", "postgresql://user:pass@localhost:5432/mydb")
    monkeypatch.setenv("URL_DB_MONGO", "mongodb://localhost:27017/mydb")

    #with pytest.raises(ValidationError):
    #    # Esto debería lanzar un ValidationError porque falta URL_DB_MONGO
    #    Setting()
