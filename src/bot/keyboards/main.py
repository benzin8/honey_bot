from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог меда"), KeyboardButton(text="Корзина")],
        [KeyboardButton(text="Регистрация")]
    ],
    resize_keyboard=True
)