def format_weather(weather: str) -> str:
    if weather == "Clear":
        return "Ясно"
    elif weather == "Rain":
        return "Дождь"
    else:
        return weather