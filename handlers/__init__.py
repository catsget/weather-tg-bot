from aiogram import Dispatcher
from handlers.start import router as start_router
from handlers.get_weather import router as get_weather_router
from handlers.change_city import router as change_city_router

def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(get_weather_router)
    dp.include_router(change_city_router)