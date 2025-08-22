from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    
    # Environment type
    TEST_ENVIRONMENT: str
    
    # MySQL database URLs
    POSTGRESQL: str
    TEST_POSTGRESQL: str
    
    # Redis database URLs
    # REDIS: str
    # TEST_REDIS: str
    
    # Telegram bot token
    BOT_TOKEN: str
    
    # LLM model
    MODEL: str
    
    model_config = SettingsConfigDict(env_file='.env')
    
    
settings = Settings()
