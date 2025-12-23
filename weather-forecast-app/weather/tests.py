# test_api.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def tests():
    # Test with a simple city
    city = "London"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(" API Key works!")
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}K")
            print(f"Weather: {data['weather'][0]['description']}")
        else:
            print(f" Error: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f" Exception: {e}")

if __name__ == "__main__":
    tests()