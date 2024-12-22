from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from keyboard import main_menu
import asyncio
from config.token import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

info = {
    "Новости": "Сегодня: курс доллара вырос на 2%, акции падают.",
    "Курсы валют": "Доллар: 87сом, Евро: 90,74сом.",
    "Контактная информация": "Наша почта: romhasanov2@gmail.com. Телефон: +996706070644.",
    "FAQ": "Часто задаваемые вопросы:\n1. Как связаться с поддержкой? — Напишите на romhasanov2@gmail.com.\n2. Где найти наш офис? — Адрес: ул. Мырзалы Аматова, Б. 1."
}

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Я информационный бот [LooT]. Вот что я умею:\n"
        "- Новости\n"
        "- Курсы валют\n"
        "- Контактная информация\n"
        "- FAQ\n"
        "Выберите нужную тему из меню ниже:",
        reply_markup=main_menu
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "/start - Приветствие и меню\n"
        "/help - Список команд\n"
        "/about - О боте\n"
        "/menu - Показать меню"
    )

@dp.message(Command("about"))
async def about_command(message: types.Message):
    await message.answer("Этот бот создан для предоставления информации. 🤖")

@dp.message(Command("menu"))
async def menu_command(message: types.Message):
    await message.answer("Выберите тему из меню:", reply_markup=main_menu)

@dp.message()
async def send_info(message: types.Message):
    if message.text in info:
        await message.answer(info[message.text])

async def main():
    print("Бот LooT . Запускается подожди немного!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
