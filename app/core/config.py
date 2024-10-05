from pydantic_settings import BaseSettings, SettingsConfigDict

# control + shif + r

class Setting(BaseSettings):
    app_name: str = "Awesome API"
    url_db_psql: str
    url_db_mongo: str
    
    model_config = SettingsConfigDict(env_file=".env")

setting = Setting()


#print(setting.url_db_psql)