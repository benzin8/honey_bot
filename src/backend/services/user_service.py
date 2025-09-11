from sqlalchemy import select
from backend.models import User
from core.database import async_session

async def create_user(telegram_id: int, name: str, username: str, phone: str = None):
    async with async_session() as session:
        result = await session.execute( # Проверка на старого пользователя
            select(User).where(User.telegram_id == telegram_id)
        )
        user = result.scalar_one_or_none()

        if user:
            print(f"Пользователь {user.telegram_id} существует")
        else:
            new_user = User(
                telegram_id = telegram_id,
                name = name,
                username = username
            )
            
            session.add(new_user)
            print(f"Новый пользователь: ID:{telegram_id}, Name: {name}, Username: {username}, Phone: {phone}")
            await session.commit()
            return new_user