from llama_index.core.tools.tool_spec.base import BaseToolSpec
import requests
import json
from datetime import datetime
import os
import calendar


class ForecastSpec(BaseToolSpec):

    spec_functions = ["forecast"]

    with open('app/engine/tools/weather/weather_codes.json', 'r') as json_file:
        weather_codes = json.load(json_file)

    def forecast(self, query:str, month:int = None, location:str = "buzet"):
        """A tool for getting forecast and weather. 
        month: pass the month user specified, if any
        location: pass the location user specified, if any
        query: Always pass the query EXACTLY as the user asked."""

        print()
        print("month: ", month)
        print("location: ", location)
        print("query: ", query)
        print("---------------------")

        url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&timesteps=1d&units=metric&apikey=yntaO7pnHyUA4DxvXhhByVwOAh2uJtKE"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)

        forecast = self.get_forecast(response)
        
        current_date_formatted = datetime.now().strftime("%d-%B-%Y")

        if month:
            historical_weather = self.historical_weather(month)
            forecast_string = f"forecast_for_six_days_starting_with_{current_date_formatted}"

            month_name = calendar.month_name[month]
            weather_string = f"weather_for_month_{month_name}"

            result = {
                "current_date": current_date_formatted,
                forecast_string : {
                    "forecast": forecast,
                    "location": response.json()['location']['name'],
                    "information": "this is historical data based on the last year."
                },
                weather_string: historical_weather
            }
        else:
            result = {
                "forecast": forecast,
                "location": response.json()['location']['name'],
                "information": "this is relevant weather forecast for next few days"
            }

        return result

    def check_day_format_date(self, date_string):
        date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = date_object.strftime("%d-%B-%Y")
        day_of_week = date_object.weekday()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        day = days_of_week[day_of_week]

        return day, formatted_date

    def get_forecast(self, response):
        forecast_arr = []
        for forecast in response.json()['timelines']['daily']:
            forecast_date = forecast['time']
            day, date = self.check_day_format_date(forecast_date)

            temp_min = round(forecast['values']['temperatureMin'])
            temp_max = round(forecast['values']['temperatureMax'])

            weather_code_min = forecast['values']['weatherCodeMin']

            forecast_string = self.weather_codes["weatherCodeFullDay"].get(str(weather_code_min), "Unknown")

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
    
    def historical_weather(self, month:int):
        with open('app/engine/tools/weather/buzet_average_temperatures_2023.json', 'r') as json_file:
            buzet_average_temperatures_2023 = json.load(json_file)

        historical_weather = buzet_average_temperatures_2023["buzet_average_temperature_year_2023"].get(str(month), "Unknown")

        result = {
            "temperature": historical_weather,
            "location": "Buzet",
            "information": "this is an estimate"
        }

        return result