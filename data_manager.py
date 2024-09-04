import requests
from pprint import pprint

sheets_prices_url = "https://api.sheety.co/ab578647650e998ab788f77b010950fe/flightDeals/prices"
sheets_users_url = "https://api.sheety.co/ab578647650e998ab788f77b010950fe/flightDeals/users"

sheet_header = {
    "Authorization": "Bearer flightdealstracker"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = sheet_header
        self.data = {}
        self.customer_data = {}

    def get_data(self):
        response = requests.get(url=sheets_prices_url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            self.data = data['prices']
            return self.data
        else:
            print("Failed to retrieve data")

    def update_destination_codes(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheets_prices_url}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=sheets_users_url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            self.customer_data = data["users"]
            return self.customer_data
        else:
            print("Failed to retrieve data")
