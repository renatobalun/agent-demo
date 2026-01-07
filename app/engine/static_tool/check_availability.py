import json
import random

def check_availability(room:str, arrival:str, departure:str, adult:str, children:str):
    
    json_result = json.dumps({
        "room": room,
        "arrival_date": arrival,
        "departure_date": departure,
        "number_of_available_rooms": random.randint(6,18),
        "details_url": "https://www.grandhotel.hr/booking",
    })

    return json_result

def get_reservation_values(data:str):
    pairs = data.split('-')

    data = {}

    for pair in pairs:
        key, value = pair.split(':')
        data[key] = value

    room = data['room']
    arrival = data['arrival']
    departure = data['departure']
    adult = data['adult']
    children = data['children']

    return room, arrival, departure, adult, children