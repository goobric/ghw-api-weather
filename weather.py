import requests

# Enter your API key here
api_key = "https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&hourly=temperature_2m"

# Enter the name of the city you want to get weather data for
city_name = "London"

# URL to fetch weather data from OpenWeatherMap API
url = f"http://api.openweathermap.org/data/2.5/weather?q={London}&appid={38fb6162099d4a3110ad8961468f84fd}"

# Fetch weather data using requests module
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Convert response to JSON format
    weather_data = response.json()

    # Print weather information
    print(f"Weather for {city_name}:")
    print(f"Temperature: {weather_data['main']['temp']} K")
    print(f"Humidity: {weather_data['main']['humidity']} %")
    print(f"Description: {weather_data['weather'][0]['description']}")
else:
    print("Error fetching weather data.")
