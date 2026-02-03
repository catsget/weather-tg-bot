from aiogram import Router, html, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from database.users import get_or_create_user

router = Router()

get_weather_button = KeyboardButton(text="Узнать погоду")
change_city = KeyboardButton(text="Поменять город")

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[get_weather_button], [change_city]], resize_keyboard=True
)

@router.message(CommandStart())
async def start_handler(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id

    await get_or_create_user(user_id)

    await message.answer(f"Приветствую, {html.bold(user_name)}", reply_markup=main_keyboard)

@router.message(F.text == "Вернуться назад")
async def go_back(message: Message, state: FSMContext):
    await state.clear()
    await start_handler(message)
