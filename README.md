# Weather Forecast Application

This Flask web application provides the current weather information for any city in the United States. The app uses the OpenWeather API to fetch weather data.

## Features
- Search weather information by city
- Displays temperature, humidity, and weather description

## How to Run the Project

1. Clone this repository.
2. Install the dependencies:
    ```bash
    pip install Flask requests python-dotenv
    ```
3. Create a `.env` file in the project root with your OpenWeather API key:
    ```
    OPENWEATHER_API_KEY=your_actual_openweather_api_key
    ```
4. Run the application:
    ```bash
    python main.py
    ```
5. Open your browser and go to `http://127.0.0.1:5000/` to use the Weather Forecast Application.

## License
This project is licensed under the MIT License.
