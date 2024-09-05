import os
import requests
from dotenv import load_dotenv

#Load env variables from .env file
load_dotenv()

#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#setup API Key
api_key = os.environ.get('OPENWEATHER_API_KEY')


if api_key is None:
    raise ValueError("Please set the env variable OPENWEATHER_API_KEY")

#set base url
base_url = "https://api.openweathermap.org/data/2.5/weather"

#construct API URL
def get_weather_data(city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params)
    return response

def main():
    city_name = input("Enter a city name: ")
    response = get_weather_data(city_name)
    if response.status_code == 200:
        try:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            city = data['name']
            description = f"{data['weather'][0]['main']}. {data['weather'][0]['description']}"

        except KeyError as e:
            print("Error: Could not find the expected data in API response")

        #Display information
        print(f"Current weather in {city}: {temperature} C.")
        print(f"Humidity: {humidity} units.")
        print(f"Description: {description}.")
    else:
        raise Exception ("ERROR WITH THE REQUEST")

main()
