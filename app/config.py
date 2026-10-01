from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    db_port: int

    class Config():
        env_file = ".env"

config = Settings() 




