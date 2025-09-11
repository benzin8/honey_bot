from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_keyboard(show_registration=True):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Каталог меда"),KeyboardButton(text="Корзина")]
        ],
        resize_keyboard=True
    )
    if show_registration:
        keyboard.keyboard.append([KeyboardButton(text="Регистрация")])
    
    return keyboard

def request_phone_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Отправить номер телефона",request_contact=True)]
        ],
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return keyboard