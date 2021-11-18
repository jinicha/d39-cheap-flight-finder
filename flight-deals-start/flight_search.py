import requests
import config
from data_manager import DataManager
# from flight_data import FlightData

API_KEY = config.API_KEY

sheet_data = DataManager().get_sheety_data()

headers = {
            "apikey": API_KEY
        }


class FlightSearch:
    def get_iata_code(self, city):
        params = {
            "term": city
        }
        response = requests.get(
            url="https://tequila-api.kiwi.com/locations/query",
            params=params,
            headers=headers)
        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def search_flight(self, fly_from, fly_to, date_from, date_to):
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "USD",
            "one_for_city": 1,
            "max_stopovers": 0,
            "sort": "price"
        }
        response = requests.get(
            url="https://tequila-api.kiwi.com/v2/search",
            params=params,
            headers=headers)

        if len(response.json()["data"]) != 0:
            data = response.json()["data"][0]
            return data
