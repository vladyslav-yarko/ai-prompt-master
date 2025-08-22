from src.utils.sa_manager import SQLAlchemyManager
from src.config import settings


class PostgreSQLManager(SQLAlchemyManager):
    SQLALCHEMY_DATABASE_URL = settings.POSTGRESQL if settings.TEST_ENVIRONMENT == "false" else settings.TEST_POSTGRESQL
    
    
sessionmanager = PostgreSQLManager()
sessionmanager.connect_to_db()
        
        
async def db_session():
    async with sessionmanager.sessions() as session:
        yield session
