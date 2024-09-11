from fastapi import APIRouter
from pydantic import PostgresDsn, MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

# control + shif + r

class Setting(BaseSettings):
    app_name: str = "Awesome API"
    url_db_psql: PostgresDsn
    url_db_mongo: str
    
    model_config = SettingsConfigDict(env_file=".env")

setting = Setting()

"""
app = APIRouter()


@app.get("/info")
def info():
    return{
        "app_name":setting.app_name,
        "url_psql": setting.url_db_psql,
        "url_mongo": setting.url_db_mongo
    }

"""