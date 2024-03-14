from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    WABAID: str
    WABATOKEN: str
    VERSION: str
    MGDB:str
    DBNAME:str

    class Config:
        env_file = './.env'

settings = Settings()
WABAURL=f"https://graph.facebook.com/{settings.VERSION}/{settings.WABAID}/messages"
WABAHEADER={"Authorization": f"Bearer {settings.WABATOKEN}","Content-Type": "application/json"}
