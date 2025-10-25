import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔑 Токен берётся из переменной окружения Render
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 🔢 Число, которое бот прибавляет к введённому пользователем
ADD_NUMBER = 2933

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет! Отправь мне число, и я прибавлю к нему 2380-347 что составит {ADD_NUMBER} 🙂")

@dp.message_handler()
async def calculate(message: types.Message):
    try:
        num = float(message.text)
        result = num + ADD_NUMBER
        await message.reply(f"{num} + {ADD_NUMBER} = {result}")
    except ValueError:
        await message.reply("Отправь число, пожалуйста 🤓")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
