from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
import os
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/1899d5724ceea3b5156ba8ba6eed8acf/flightDeals" 


PASSWORD =  os.environ["GOOGLE_SHEETS_PASS"]
USER = os.environ["GOOGLE_SHEETS_USER"]
basic = HTTPBasicAuth(USER,PASSWORD)

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        link = SHEETY_PRICES_ENDPOINT + "/prices"
        response = requests.get(url=link,auth=basic)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            link = SHEETY_PRICES_ENDPOINT + "/prices"

            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{link}/{city['id']}",
                json=new_data,
                auth=basic
            )
            print(response.text)
    
    def get_mail(self):
        link = SHEETY_PRICES_ENDPOINT + "/users"
        response = requests.get(
            url=link,
            auth=basic
        )
        return response.json()
