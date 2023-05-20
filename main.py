import os
import datetime
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import config


bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Hello! Im Weatheriano')

@dp.message_handler()
async def get_weather(message: types.Message):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&units=metric&APPID={config.weather_api_token}'
    response = requests.get(url)
    data = response.json()
    city = data['name']
    cur_temp = data['main']['temp']
    await message.reply(data)


if __name__ == '__main__':
    executor.start_polling(dp)