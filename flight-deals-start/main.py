# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
import config
from data_manager import DataManager
from flight_search import FlightSearch

TOKEN = config.TOKEN

base_url = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/prices/"

sheet_data = DataManager().get_sheety_data()
flight_search = FlightSearch()

sheety_headers = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-type": "application/json"
}

for data in sheet_data:
    if not data["iataCode"]:
        city_name = data["city"]
        city_id = str(data["id"])
        body = {
            "price": {
                "iataCode": flight_search.get_iata_code(city_name)
            }
        }

        requests.put(url=base_url + city_id, headers=sheety_headers, json=body)
