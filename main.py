from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Access the API key from environment variables

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    if request.method == 'POST':
        city = request.form['city']
        country = 'US'
        full_city_name = f"{city},{country}"  # Country code for API recognition
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather',
                                params={'q': full_city_name, 'appid': API_KEY, 'units': 'imperial'})
        if response.status_code == 200:
            weather_data = response.json()
            if 'main' not in weather_data or 'weather' not in weather_data:
                error_message = "Unable to fetch weather data. Please try again."
        else:
            error_message = "City not found. Please enter a valid city name."

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
