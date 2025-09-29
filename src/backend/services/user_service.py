from sqlalchemy import select
from backend.models import User
from core.database import async_session

async def create_user(telegram_id: int, name: str, username: str, phone: str = None):
    async with async_session() as session:
        """
        Old user checker
        """
        result = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )

        user = result.scalar_one_or_none() # True или False
        print(user)

        """
        Update data
        """
        if user is not None:
            if phone is not None and user.phone != phone:
                user.phone = phone
            if user.name != name:
                user.name = name
            if user.username != username:
                user.username = username
            await session.commit()
            return user
        else:
            user = User(
                telegram_id = telegram_id,
                name = name,
                username = username,
                phone = phone,
            )
            
            session.add(user)
            print(f"Новый пользователь: ID:{telegram_id}, Name: {name}, Username: {username}, Phone: {phone}")
            await session.commit()