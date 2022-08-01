#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from amadeus import Client, ResponseError
from flight_search import FlightSearch
from data_manager import DataManager

API_KEY = "9vC8YC7b8zC1huvcRLVOik39PzwhAyBK"
API_SECRET = "l9NH28dtIGEh2aYP"

amadeus_client = Client(client_id=API_KEY, client_secret=API_SECRET)
data_manager = DataManager(amadeus_client)
flight_search = FlightSearch(amadeus_client)

data_manager.add_IATA_codes()