from fastapi import APIRouter
from pydantic_settings import BaseSettings, SettingsConfigDict

# control + shif + r

class Setting(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "default"
    model_config = SettingsConfigDict(env_file=".env")


setting = Setting()
app = APIRouter()


@app.get("/info")
def info():
    return{
        "app_name":setting.app_name,
        "admin_email":setting.admin_email
        #"items_per_user":setting.items_per_user
    }