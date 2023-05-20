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
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    weather = weather[0].upper() + weather[1:]
    wind = data['wind']['speed']
    clean_data = f'{city}: \n' \
                 f'{weather}\n' \
                 f'Температура: {temp} C\u00b0 \n' \
                 f'Скорость ветра: {wind} м/с'

    print(data)
    print(clean_data)
    print()
    await message.reply(clean_data)


if __name__ == '__main__':
    executor.start_polling(dp)
