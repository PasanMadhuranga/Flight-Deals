import json
from datetime import timedelta, date

import requests

ORIGIN_CITY = "LON"
TEQUILA_API_KEY = "HcHDQ-0lzJRWUQn3_M3DLwQeSYuBePfb"

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day

# Get the month and the year after six months.
if current_month + 6 > 12:
    end_month = current_month - 6
    end_year = current_year + 1
else:
    end_month = current_month + 6
    end_year = current_year

from_date = date(current_year, current_month, current_day)
to_date = date(end_year, end_month, current_day)

headers = {
    "apikey": TEQUILA_API_KEY
}
flight_search_end_point = "https://tequila-api.kiwi.com/v2/search"
parameters = {
    "fly_from": ORIGIN_CITY,
    "fly_to": "PAR",
    "date_from": from_date.strftime("%d/%m/%Y"),
    "date_to": to_date.strftime("%d/%m/%Y"),
    "price_to": 60,
    "adults": 2,
}

response = requests.get(url=flight_search_end_point, params=parameters, headers=headers)
data = response.json()["data"]
print(data)
# print(json.dumps(data, sort_keys=4, indent=4))

# for flight in data:
#     print(flight["price"])
# print(json.dumps(data, sort_keys=4, indent=4))













# import json
#
# from amadeus import Client, ResponseError
#
# API_KEY = "9vC8YC7b8zC1huvcRLVOik39PzwhAyBK"
# API_SECRET = "l9NH28dtIGEh2aYP"
#
# amadeus = Client(
#     client_id=API_KEY,
#     client_secret=API_SECRET
# )
#
# try:
#     '''
#     Returns price metrics of a given itinerary
#     '''
#     response = amadeus.analytics.itinerary_price_metrics.get(originIataCode='PAR',
#                                                              destinationIataCode='SFO',
#                                                              departureDate='2022-11-21')
#     print(response.data)
# except ResponseError as error:
#     raise error
