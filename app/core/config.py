from pydantic_settings import BaseSettings, SettingsConfigDict
import secrets

# control + shif + r

class Setting(BaseSettings):
    app_name: str = "Awesome API"
    url_db_psql: str
    url_db_mongo: str
    algorithm: str
    secret_key: str
    #secret_key = secrets.token_hex()

    model_config = SettingsConfigDict(env_file=".env")
