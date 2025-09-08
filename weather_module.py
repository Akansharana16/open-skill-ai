import requests
from stt import speak

def get_weather(city="Delhi"):
    api_key = "629fe03d775e8764ce019058e2163db7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get("main"):
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
        weather_report = f"The temperature in {city} is {temp}°C with {desc}."
        print(weather_report)
        return weather_report
    else:
        return "Could not fetch weather."

# Call like this:
speak(get_weather("Mumbai"))
