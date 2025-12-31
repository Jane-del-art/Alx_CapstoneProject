import os
from dotenv import load_dotenv

def validate_api_key():
    """Check if API key is properly configured"""
    load_dotenv()
    
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    
    if not api_key:
        return False, "API key not found in environment variables"
    
    if api_key == 'your_actual_api_key_here':
        return False, "Please replace 'your_actual_api_key_here' with your actual OpenWeatherMap API key"
    
    return True, "API key is configured"
