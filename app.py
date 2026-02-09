from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "28491ae5148ab30cd6fee86750eac50e"
CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def fetch_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    weather = requests.get(CURRENT_URL, params=params).json()
    forecast = requests.get(FORECAST_URL, params=params).json()
    return weather, forecast


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")
        weather, forecast = fetch_weather(city)

        if weather.get("cod") != 200:
            return render_template("error.html")

        daily = forecast["list"][::8][:5]
        return render_template(
            "weather.html",
            city=weather["name"],
            country=weather["sys"]["country"],
            temp=weather["main"]["temp"],
            desc=weather["weather"][0]["description"].title(),
            wind=weather["wind"]["speed"],
            forecast=daily,
            date=datetime.now().strftime("%A, %B %d"),
        )

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
