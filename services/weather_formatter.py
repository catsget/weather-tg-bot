def format_weather(weather: str) -> str:
    if weather == "Clear":
        return "Ясно"
    elif weather == "Rain":
        return "Дождь"
    elif weather == "Clouds":
        return "Облачно"
    else:
        return weather