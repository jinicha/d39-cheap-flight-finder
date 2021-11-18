import requests
import config

TOKEN = config.TOKEN

sheety_url = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/prices"
sheety_header = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-type": "application/json"
}


class DataManager:
    def __init__(self):
        self.sheety_data = {}

    def get_sheety_data(self):
        response = requests.get(url=sheety_url, headers=sheety_header)
        self.sheety_data = response.json()["prices"]
        return self.sheety_data
