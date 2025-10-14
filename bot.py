from aiogram import Bot, Dispatcher, types, executor
import sqlite3
from config import BOT_TOKEN, DB_PATH
from database import init_db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
init_db()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "👨‍🍳 Привет, шеф!\n\nДобро пожаловать в *CookNet AI!*",
        parse_mode="Markdown",
        reply_markup=types.ReplyKeyboardMarkup(
            resize_keyboard=True
        ).add(
            types.KeyboardButton("🍳 Добавить рецепт"),
            types.KeyboardButton("📖 Мои рецепты"),
            types.KeyboardButton("❤️ Топ рецептов")
        )
    )

@dp.message_handler(lambda m: m.text == "🍳 Добавить рецепт")
async def add_recipe(message: types.Message):
    await message.answer("Отправь название рецепта:")

@dp.message_handler(lambda m: m.text == "❤️ Топ рецептов")
async def top_recipes(message: types.Message):
    await message.answer("Пока нет данных, но скоро появятся ❤️")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
