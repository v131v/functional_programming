import os
import requests
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    await message.answer(
        "Привет! Я бот. Введите /weather <город> или /exchange для получения данных."
    )


@dp.message_handler(commands=["weather"])
async def handle_weather(message: types.Message):
    if len(message.text.split()) < 2:
        await message.answer("Использование: /weather <город>")
        return

    city = message.text.split()[1]
    weather_data = get_weather(city)

    if weather_data:
        temperature = weather_data["current"]["temp_c"]
        await message.answer(f"Текущая температура в {city}: {temperature}°C")
        logger.info(f"User {message.from_user.username} requested weather in {city}.")
    else:
        await message.answer(f"Не удалось получить данные о погоде для {city}.")
        logger.error(f"Failed to fetch weather data for {city}.")


@dp.message_handler(commands=["exchange"])
async def handle_exchange(message: types.Message):
    exchange_rates_data = get_exchange_rates()

    if exchange_rates_data:
        rates_text = "\n".join(
            [
                f"{currency}: {rate['Value']} {rate['CharCode']}"
                for currency, rate in exchange_rates_data["Valute"].items()
            ]
        )
        await message.answer(f"Курсы валют:\n{rates_text}")
        logger.info(f"User {message.from_user.username} requested exchange rates.")
    else:
        await message.answer("Не удалось получить данные о курсах валют.")
        logger.error("Failed to fetch exchange rates data.")


def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        return None


def get_exchange_rates():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        logger.error(f"Error fetching exchange rates data: {e}")
        return None


if __name__ == "__main__":
    load_dotenv(".env")
    executor.start_polling(dp, skip_updates=True)
