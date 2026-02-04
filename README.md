## Weather Telegram Bot
### About
Asynchronous bot written with libraries: **aiogram**, **asyncpg** \
Using OpenWeatherMap API

You need create table **users** for working database
```
CREATE TABLE users (
  user_id BIGINT PRIMARY KEY,
  user_city VARCHAR(30)
)
```
### Requirements
- Python 3.10+
- PostgreSQL
- Redis
### Setup
1. Clone repository
```
git clone https://github.com/catsget/weather-tg-bot.git
```
2. Create and setup `.env` using `.env.example`
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the bot
```
python main.py
```
