from pydantic_settings import BaseSettings, SettingsConfigDict
from opt.constants.environment import Environment
from os import getcwd

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', env_prefix='TELEGRAM_BOT_')
    
    PATH: str = getcwd()
    ENVIROMENT: Environment = Environment.LOCAL
    TRY_TIME: int = 3
    API_KEY: str = 'API_KEY'
    USERNAME: str = 'NAME'
    


config = Config()