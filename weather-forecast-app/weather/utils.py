import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv('c650fc2460db7d607892b1584d908c4a')

# Example usage
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Test it
if __name__ == "__main__":
    weather = get_weather("London")
    print(weather)