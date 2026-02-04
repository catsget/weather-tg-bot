import database as db


async def get_user(telegram_id: int):
    async with db.pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE user_id = $1", telegram_id
        )


async def create_user(telegram_id: int):
    async with db.pool.acquire() as conn:
        return await conn.fetchrow(
            """
            INSERT INTO users (user_id)
            VALUES ($1)
            RETURNING *
            """,
            telegram_id,
        )


async def get_or_create_user(telegram_id: int):
    user = await get_user(telegram_id)
    if user:
        return user
    return await create_user(telegram_id)


async def update_city(telegram_id: int, city: str):
    async with db.pool.acquire() as conn:
        await conn.execute(
            "UPDATE users SET user_city = $1 WHERE user_id = $2", city, telegram_id
        )


async def get_city(telegram_id: int):
    async with db.pool.acquire() as conn:
        return await conn.fetchrow(
            """
            SELECT user_city FROM users WHERE user_id = $1
            """,
            telegram_id,
        )
