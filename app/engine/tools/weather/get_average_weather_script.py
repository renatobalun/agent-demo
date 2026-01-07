import requests
import json

url = "https://archive-api.open-meteo.com/v1/archive"

buzet_location = [45.4094, 13.9667] 
result_dict = {"buzet_average_temperature_year_2023": {}}

for n in range(12):
    day = "30" if not n + 1 == 2 else "28" 
    month = str(n + 1).zfill(2)

    params = {
        "latitude": buzet_location[0],
        "longitude": buzet_location[1],
        "start_date": f"2023-{month}-01",
        "end_date": f"2023-{month}-{day}",
        "daily": ["apparent_temperature_min", "apparent_temperature_max"]
    }

    response = requests.get(url, params=params)
    data = response.json()

    avg_min_temp = round(sum(data['daily']['apparent_temperature_min']) / len(data['daily']['apparent_temperature_min']))
    avg_max_temp = round(sum(data['daily']['apparent_temperature_max']) / len(data['daily']['apparent_temperature_max']))

    result_dict["buzet_average_temperature_year_2023"][f"{month}"] = {"min": avg_min_temp, "max": avg_max_temp}

with open("buzet_average_temperatures_2023.json", "w") as json_file:
    json.dump(result_dict, json_file, indent=4)
