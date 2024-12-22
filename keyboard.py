from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Новости"), KeyboardButton(text="Курсы валют")],
        [KeyboardButton(text="Контактная информация"), KeyboardButton(text="FAQ")]
    ],
    resize_keyboard=True
)
