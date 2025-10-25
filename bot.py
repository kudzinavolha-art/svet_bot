import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# 🔑 Токен берётся из переменной окружения Render
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# 🔢 Число, которое бот прибавляет к введённому пользователем
ADD_NUMBER = 2933

# Команда /start
@dp.message(Command(commands=["start"]))
async def send_welcome(message: Message):
    await message.answer(
        f"Привет! Отправь мне число, и я прибавлю к нему 2380-347 что составит {ADD_NUMBER} 🙂"
    )

# Обработка любых сообщений
@dp.message()
async def calculate(message: Message):
    try:
        num = float(message.text)
        result = num + ADD_NUMBER
        await message.answer(f"{num} + {ADD_NUMBER} = {result}")
    except ValueError:
        await message.answer("Отправь число, пожалуйста 🤓")

# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
