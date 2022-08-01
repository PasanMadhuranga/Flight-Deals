import json

from amadeus import Client, ResponseError

API_KEY = "9vC8YC7b8zC1huvcRLVOik39PzwhAyBK"
API_SECRET = "l9NH28dtIGEh2aYP"

amadeus = Client(
    client_id=API_KEY,
    client_secret=API_SECRET
)

try:
    '''
    Returns price metrics of a given itinerary
    '''
    response = amadeus.analytics.itinerary_price_metrics.get(originIataCode='PAR',
                                                             destinationIataCode='SFO',
                                                             departureDate='2022-11-21')
    print(response.data)
except ResponseError as error:
    raise error
