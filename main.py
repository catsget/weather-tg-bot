import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from handlers import register_routes
from database import init_db

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

redis = Redis(host="localhost")
storage = RedisStorage(redis=redis)

dp = Dispatcher(storage=storage)

async def main():
    await init_db()

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    register_routes(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
