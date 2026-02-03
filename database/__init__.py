import asyncpg
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

pool: asyncpg.Pool | None = None

async def init_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

async def close_db():
    await pool.close()