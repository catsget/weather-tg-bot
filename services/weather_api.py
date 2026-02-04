import aiohttp
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv("WEATHER_API_TOKEN")

async def get_weather(city: str) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&type=like&lang=ru&APPID={TOKEN}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()