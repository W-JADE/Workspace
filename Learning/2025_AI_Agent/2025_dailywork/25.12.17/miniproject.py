# 보조.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_busan_weather() -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "OPENWEATHER_API_KEY가 .env에 없습니다."
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Busan,KR",
        "appid": api_key,
        "units": "metric",
        "lang": "kr",
    }
    
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code != 200:
            return f"OpenWeather API 오류: {r.status_code} / {r.text}"

        data = r.json()

        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        hum = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        return (
            f"서울 현재 날씨: {desc}, "
            f"기온: {temp:.1f}℃ (체감 {feels:.1f}℃), "
            f"습도: {hum}%, 풍속: {wind:.1f}㎧"
        )

    except Exception as e:
        return f"날씨 조회 예외: {type(e).__name__}: {e}"


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_busan_weather",
            "description": "부산(대한민국)의 현재 날씨를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {}
            },
        },
    }
]
