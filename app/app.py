from flask import Flask, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather/<city>')
def weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return jsonify({"error": "No API key set"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},LK&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code
    
    data = response.json()

    pretty_data = {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temperature_celsius": data.get("main", {}).get("temp"),
        "feels_like_celsius": data.get("main", {}).get("feels_like"),
        "humidity_percent": data.get("main", {}).get("humidity"),
        "weather_description": data.get("weather", [{}])[0].get("description"),
        "wind_speed_mps": data.get("wind", {}).get("speed"),
        "cloud_coverage_percent": data.get("clouds", {}).get("all")
    }

    return jsonify(pretty_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
