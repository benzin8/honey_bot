from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards import main_keyboard, request_phone_keyboard

registration_router = Router()

@registration_router.message(F.text == "Регистрация")
async def start_registration(message: Message):
    await message.answer(
        "Для реистрации требуется ваш номер телефона:",
        reply_markup=request_phone_keyboard()
    )