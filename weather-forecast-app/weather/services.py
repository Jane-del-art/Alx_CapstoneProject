import os
import requests
from pathlib import Path
from dotenv import load_dotenv

def get_weather_data(city_name):
    """
    Fetch weather data from OpenWeatherMap API
    """
    # Load .env file
    project_root = Path(__file__).resolve().parent.parent
    env_path = project_root / '.env'
    
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    else:
        # Try loading from current directory
        load_dotenv()
    
    # Get API key from environment
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        # Show helpful error message
        raise Exception(
            f"❌ API Key not found!\n\n"
            f"Please create a '.env' file in:\n"
            f"   {project_root}\n\n"
            f"With this content:\n"
            f"   OPENWEATHER_API_KEY=your_actual_api_key_here\n\n"
            f"Get a free key from: https://openweathermap.org/api"
        )
    
    if api_key == 'your_actual_api_key_here':
        raise Exception(
            f"⚠️  You're using the placeholder API key!\n\n"
            f"Please edit:\n"
            f"   {env_path}\n\n"
            f"And replace 'your_actual_api_key_here' with your actual API key.\n"
            f"Get a free key from: https://openweathermap.org/api"
        )
    
    # Now use the API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if response.status_code != 200:
            error_msg = data.get('message', 'Unknown error')
            if response.status_code == 401:
                raise Exception(f"❌ Invalid API Key: {error_msg}")
            elif response.status_code == 404:
                raise Exception(f"❌ City '{city_name}' not found")
            else:
                raise Exception(f"❌ API Error: {error_msg}")
        
        return {
            'city_name': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'weather_description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure'],
        }
        
    except Exception as e:
        raise Exception(f"❌ Error: {str(e)}")