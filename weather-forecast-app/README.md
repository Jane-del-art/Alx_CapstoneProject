# Weather Forecast App

A Django-based weather forecasting application for ALX Capstone Project.

## Features
- Current weather display
- 5-day weather forecast
- City-based weather search
- Responsive Django interface

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate it: `source venv/Scripts/activate` (Windows Git Bash)
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`: `cp .env.example .env`
6. Get OpenWeatherMap API key: https://openweathermap.org/api
7. Add your API key to `.env`: `OPENWEATHER_API_KEY=your_key_here`

## API Testing
Run `python tests.py` to test your OpenWeatherMap API connection.

# Add it
git add README.md
git commit -m "Add project README with setup instructions"