# 🌦️ Realtime Global Weather App

A modern, containerized Flask web app that fetches real-time weather data for any city in the world using the OpenWeatherMap API. Built with Flask, Docker, and styled with a modern UI using HTML + CSS.

---

## 🚀 Features

- 🔎 Get live weather by entering any city
- 📍 Defaults to cities in Sri Lanka (`Colombo`, `Galle`, etc.)
- 🌐 Expandable to global cities (e.g., `New York`, `Tokyo`, etc.)
- 💅 Clean, responsive, modern UI
- 🐳 Fully Dockerized for easy deployment
- 🔒 Uses `.env` file for API key management

---

## 📁 Project Structure

```plaintext
hemlProject/
│   Dockerfile
│   README.md
│
├───app
│   ├── app.py
│   ├── .env
│   ├── requirements.txt
│   └── templates
│       └── index.html
│
└───helm
    └── weather-app
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── deployment.yaml
            ├── service.yaml
            ├── NOTES.txt
            └── _helpers.tpl
