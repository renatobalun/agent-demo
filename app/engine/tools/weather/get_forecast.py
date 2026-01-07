import requests
import json
from datetime import datetime
import os

url = "https://api.tomorrow.io/v4/weather/forecast?location=zagreb&timesteps=1d&units=metric&apikey=yntaO7pnHyUA4DxvXhhByVwOAh2uJtKE"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

with open('app/engine/tools/weather/weather_codes.json', 'r') as json_file:
    weather_codes = json.load(json_file)

def check_day_format_date(date):
    date_string = date
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    day_of_week = date_object.weekday()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day = days_of_week[day_of_week]
    formatted_date = date_object.strftime("%d-%m-%Y")
    return day, formatted_date

def get_forecast(response):
    forecast_arr = []
    for forecast in response.json()['timelines']['daily']:
        forecast_date = forecast['time']
        day, date = check_day_format_date(forecast_date)

        temp_min = round(forecast['values']['temperatureMin'])
        temp_max = round(forecast['values']['temperatureMax'])

        weather_code_min = forecast['values']['weatherCodeMin']

        forecast_string = weather_codes["weatherCodeFullDay"].get(str(weather_code_min), "Unknown")

        image_folder_path = "app/engine/tools/weather/weather_images"
        all_files = os.listdir(image_folder_path)
        matching_files = [file for file in all_files if file.startswith(str(f"{weather_code_min}0"))]

        forecast_json = {
            "date": date,
            "day": day,
            "temperatureMin": temp_min,
            "temperatureMax": temp_max,
            "weather_forecast": forecast_string,
            "weather_image": matching_files[0]
        }

        forecast_arr.append(forecast_json)
    
    return forecast_arr


forecast = get_forecast(response)

result = {
    "forecast": forecast,
    "location": response.json()['location']['name']
}