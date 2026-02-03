from aiogram import Router, F
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.start import start_handler
from database.users import update_city

router = Router()

go_back_button = KeyboardButton(text="Вернуться назад")

go_back_keyboard = ReplyKeyboardMarkup(
    keyboard=[[go_back_button]], resize_keyboard=True
)


class WeatherStates(StatesGroup):
    waiting_for_new_city = State()


@router.message(F.text == "Поменять город")
async def change_city(message: Message, state: FSMContext):
    await message.answer("Выберите город", reply_markup=go_back_keyboard)
    await state.set_state(WeatherStates.waiting_for_new_city)


@router.message(WeatherStates.waiting_for_new_city)
async def change_user_info(message: Message, state: FSMContext):
    city = message.text
    user_id = message.from_user.id

    if city:
        await update_city(user_id, city)
        await message.answer("Город успешно обновлен")
        await state.clear()
        await start_handler(message)
