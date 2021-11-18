import requests
import config
from data_manager import DataManager

API_KEY = config.API_KEY

base_url = "https://tequila-api.kiwi.com/locations/query"

sheet_data = DataManager().get_sheety_data()


class FlightSearch:
    def get_iata_code(self, city):
        headers = {
            "apikey": API_KEY
        }
        params = {
            "term": city
        }
        response = requests.get(url=base_url, params=params, headers=headers)
        iata_code = response.json()["locations"][0]["code"]
        print(iata_code)
        return iata_code
