import requests
import json

# Replace with your own OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data
def get_weather(city_name):
    # Constructing the complete URL for the API request
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"  # Using 'metric' for Celsius temperatures
    
    # Make a GET request to the API
    response = requests.get(complete_url)
    
    # Parse the response JSON
    data = response.json()
    
    # Check if the request was successful
    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Extract relevant information
        city = data["name"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]
        
        # Display weather details
        print(f"Weather in {city}:\n")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}\n")
    else:
        print("City not found or invalid API key.")

# Main execution block
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
