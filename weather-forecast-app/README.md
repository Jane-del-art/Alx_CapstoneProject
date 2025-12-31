WeatherCast - Weather Forecast Web Application
A modern, feature-rich weather forecast web application built with Django that provides real-time weather information for cities worldwide using the OpenWeatherMap API.

🚀 Features
✅ Core Features
Real-time Weather Search: Get current weather for any city worldwide

Detailed Weather Information: Temperature, humidity, wind speed, pressure, and conditions

Search History: Automatically saves all your searches for quick reference

Clear History: Option to delete all search records

🎨 User Experience
Responsive Design: Works perfectly on desktop, tablet, and mobile

Modern UI: Beautiful gradient designs with smooth animations

Intuitive Navigation: Easy-to-use interface with clear navigation

Error Handling: User-friendly error messages for invalid searches

🔧 Technical Features
Django MVT Architecture: Clean separation of concerns

API Integration: OpenWeatherMap Current Weather Data API

Database Storage: SQLite with Django ORM

Environment Configuration: Secure API key management with .env files

Static File Management: Organized CSS and JavaScript

🛠️ Technology Stack
Backend
Framework: Django 5.2.7

Language: Python 3.11+

Database: SQLite (Development), PostgreSQL/MySQL ready

API: OpenWeatherMap Current Weather Data API

Authentication: Django session-based

Frontend
Styling: Bootstrap 5.2, Custom CSS

Icons: Font Awesome 6.0

JavaScript: Vanilla JS for interactivity

Responsive: Mobile-first design

Development Tools
Version Control: Git & GitHub

Environment: python-dotenv

API Testing: Requests library

 Quick Start
Prerequisites
Python 3.11 or higher

Git

OpenWeatherMap API key (free)

Installation
Clone the repository

bash
git clone https://github.com/yourusername/weather-forecast-app.git
cd weather-forecast-app
Create virtual environment

bash
python -m venv venv

# On Windows:
venv\Scripts\activate

Install dependencies

bash
pip install -r requirements.txt
Set up environment variables

bash
# Copy the example file
cp .env.example .env

# Edit .env and add your OpenWeatherMap API key
# Get free API key from: https://openweathermap.org/api
Run migrations

bash
python manage.py migrate
Create superuser (optional)

bash
python manage.py createsuperuser
Run development server

bash
python manage.py runserver
Visit the application
Open http://127.0.0.1:8000 in your browser

🔑 API Configuration
Get a free API key from OpenWeatherMap

Sign up for the free tier (1,000 calls/day)

Verify your email address

Copy your API key from API Keys page

Add to your .env file:

text
OPENWEATHER_API_KEY=your_actual_api_key_here
📱 Application Pages
🏠 Home Page (/)
Search form for weather information

Features overview with icons

Quick statistics

Responsive design

🌡️ Weather Results (/weather/)
Current temperature with gradient display

Weather conditions and description

Humidity and wind speed

Local time display

Action buttons for new search/view history

📜 Search History (/history/)
Table view of all previous searches

City, temperature, weather, humidity, wind, country, and timestamp

Clear history functionality

Empty state with call-to-action

 Error Page
User-friendly error messages

Troubleshooting tips

Action buttons to try again or view history

 Running Tests
bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test weather

🔧 Development
Adding New Features
Create/update models in models.py

Create migrations: python manage.py makemigrations

Apply migrations: python manage.py migrate

Update views in views.py

Create/update templates in templates/weather/

Update URL routing in urls.py

Code Style
Follow Django coding style guidelines

Use meaningful variable names

Add comments for complex logic

Keep functions focused and small

🐛 Troubleshooting
Common Issues
Issue	Solution
API Key not found	Check .env file exists and has correct variable name
Static files not loading	Run python manage.py collectstatic
Database errors	Run python manage.py migrate
Module not found	Activate virtual environment: source venv/bin/activate
Debug Mode
For development, set in settings.py:

python
DEBUG = True
For production, always set:

python
DEBUG = False
📄 API Reference
OpenWeatherMap API
Endpoint: https://api.openweathermap.org/data/2.5/weather

Parameters: q={city}&appid={API_KEY}&units=metric

Response Format: JSON

Rate Limit: 60 calls/minute (free tier)

Data Extracted
City name

Country code

Temperature (°C)

Weather description

Humidity (%)

Wind speed (m/s)

Atmospheric pressure (hPa)

🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m 'Add amazing feature'

Push to branch: git push origin feature/amazing-feature

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👤 Author
Jane Nwachukwu

GitHub: @yourusername

LinkedIn: Jane Nwachukwu

Portfolio: yourportfolio.com

🙏 Acknowledgments
OpenWeatherMap for the free weather API

Django for the amazing web framework

Bootstrap for the UI components

Font Awesome for the beautiful icons

ALX Africa for the learning opportunity

🎓 Capstone Project
This project was developed as part of the ALX Software Engineering Program Capstone Project. It demonstrates comprehensive full-stack web development skills using Django, API integration, database management, and responsive design.

Project Requirements Met:
✅ Django web application with MVT architecture

✅ External API integration (OpenWeatherMap)

✅ Database operations with Django ORM

✅ User authentication (session-based)

✅ Responsive frontend design

✅ Error handling and validation

✅ Deployment ready

Learning Outcomes:
Full-stack Django development

API consumption and data parsing

Database design and migrations

Frontend development with Bootstrap

Deployment and hosting configuration

Problem-solving and debugging

Happy Weather Forecasting! ☀️🌧️❄️🌪️
