from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards import main_keyboard
from backend.services import create_user

start_router = Router()

@start_router.message(Command("start"))
async def cmd_start(message: Message):
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    user = await create_user(
        telegram_id=telegram_id,
        name = first_name,
        username=username
    )

    show_registration = user.phone is None

    await create_user(telegram_id, first_name, username)
    await message.answer(f"Добро пожаловать в магазин меда, {first_name}! Выберете действие:", reply_markup=main_keyboard(show_registration=show_registration))
