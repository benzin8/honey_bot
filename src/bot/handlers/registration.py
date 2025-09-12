from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import main_keyboard, request_phone_keyboard
from backend.services import create_user

registration_router = Router()

@registration_router.message(F.text == "Регистрация")
async def start_registration(message: Message):
    await message.answer(
        "Для регистрации требуется ваш номер телефона:",
        reply_markup=request_phone_keyboard()
    )

@registration_router.message(F.contact)
async def add_phone(message: Message):
    contact = message.contact

    await create_user(
        telegram_id = contact.user_id,
        name = contact.first_name,
        username = message.from_user.username,
        phone = contact.phone_number
    )

    await message.answer(
        "Регистрация завершена!",
        reply_markup=main_keyboard(show_registration=False)
    )