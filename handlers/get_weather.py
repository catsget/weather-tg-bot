from aiogram import Router, F, html
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from services.weather_api import get_weather
from database.users import get_city

router = Router()


@router.message(F.text == "Узнать погоду")
async def get_weather_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    city = (await get_city(user_id))[0]

    if city:
        weather = await get_weather(city)

        if weather["cod"] == "200" and len(weather["list"]) > 0:
            weather_info = weather["list"][0]

            await message.answer(
                f"{city}\n\n{html.bold('Температура')}\n{int(weather_info['main']['temp'])} градусов\n\n{html.bold('Скорость ветра')}\n{int(weather_info['wind']['speed'])} м/с"
            )
            await state.clear()
        else:
            await message.answer("Город не указан или не существует")
