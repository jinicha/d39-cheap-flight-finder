# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import requests
import config
from data_manager import DataManager
from flight_search import FlightSearch

TOKEN = config.TOKEN

base_url = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/prices/"

sheet_data = DataManager()
data = sheet_data.get_sheety_data()
test = FlightSearch()

sheety_header = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-type": "application/json"
}
for item in data:
    if not item["iataCode"]:
        city_id = item["id"]
        body = {
            "price": {
                "iataCode": test.test()
            }
        }

        requests.put(url=base_url + city_id, headers=sheety_header, json=body)
