#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from amadeus import Client, ResponseError
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

API_KEY = "9vC8YC7b8zC1huvcRLVOik39PzwhAyBK"
API_SECRET = "l9NH28dtIGEh2aYP"

amadeus_client = Client(client_id=API_KEY, client_secret=API_SECRET)
data_manager = DataManager(amadeus_client)
flight_search = FlightSearch(amadeus_client)

# data_manager.add_IATA_codes()
# iata_and_price = data_manager.get_rows()
# print(iata_and_price)
available_flights_objects = flight_search.all_flights_available(data_manager.get_rows())
notification_manager = NotificationManager(available_flights_objects)
notification_manager.send_notifications()