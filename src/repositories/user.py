from typing import Optional

from src.utils.repository import SQLAlchemyRepository
from src.models import User


class UserRepository(SQLAlchemyRepository):
    model = User
    
    async def get_one_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        user = await self.get_one(telegramId=telegram_id)
        return user
