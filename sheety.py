import os
import requests
from requests.auth import HTTPBasicAuth

#Config

USER = os.environ["GOOGLE_SHEETS_USER"]
PASSWORD = os.environ["GOOGLE_SHEETS_PASS"]
LINK = "https://api.sheety.co/1899d5724ceea3b5156ba8ba6eed8acf/flightDeals/users"
basic = HTTPBasicAuth(USER,PASSWORD)

#DATA
class Users:
    def __init__(self,user_name,user_last_name,user_email):
        self.firstName = user_name
        self.lastName = user_last_name
        self.email = user_email
        self.body = {
            "user":{
                "firstName":user_name,
                "lastName" : user_last_name,
                "email" : user_email}
                }
    def load_info(self):
        response = requests.post(
            url=LINK,
            json=self.body,
            auth=basic)
        response.raise_for_status()
        print(response.json())
