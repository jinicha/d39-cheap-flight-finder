import requests
import datetime as dt
import config
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

TOKEN = config.TOKEN
API_KEY = config.API_KEY
CITY_FROM = "London"
CITY_FROM_CODE = "LON"

sheet_data = DataManager().get_sheety_data()
flight_search = FlightSearch()
send_notification = NotificationManager()

search_iata_code_url = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/prices/"

tomorrow = dt.date.today() + dt.timedelta(days=1)
six_months_after = tomorrow + dt.timedelta(days=180)

sheety_put_headers = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-type": "application/json"
}
search_flight_headers = {
    "apikey": API_KEY
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
        requests.put(url=search_iata_code_url + city_id, headers=sheety_put_headers, json=body)
    else:
        flight = flight_search.search_flight(
            CITY_FROM_CODE,
            data["iataCode"],
            tomorrow.strftime("%d/%m/%Y"),
            six_months_after.strftime("%d/%m/%Y")
        )
        if flight:
            price = flight["price"]
            fly_from = flight["flyFrom"]
            city_to = flight["cityTo"]
            fly_to = flight["flyTo"]
            from_date = flight["route"][0]["local_departure"].split('T')[0]
            to_date = flight["route"][1]["local_departure"].split('T')[0]
            if price < data["lowestPrice"]:
                send_notification.send_message(
                    f'Low price alert! Only ${price} to fly from {CITY_FROM}-{fly_from} to {city_to}-{fly_to}, from {from_date} to {to_date}.'
                )
            else:
                send_notification.send_message(
                    f'It is not a great time to travel to {city_to} :('
                )
