import time

import requests
from amadeus import Client, ResponseError
from datetime import timedelta, date
from flight_data import FlightData

ORIGIN_CITY_CODE = "LON"
ORIGIN_CITY = "London"
TEQUILA_API_KEY = "HcHDQ-0lzJRWUQn3_M3DLwQeSYuBePfb"

class FlightSearch:
    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_API_KEY
        }

    def all_flights_available(self, rows: list) -> list:
        """Return a list of available flights as FlightData objects."""
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

        flight_search_end_point = "https://tequila-api.kiwi.com/v2/search"
        available_flights = []
        for row in rows:
            parameters = {
                "fly_from": ORIGIN_CITY_CODE,
                "fly_to": row["iataCode"],
                "date_from": from_date.strftime("%d/%m/%Y"),
                "date_to": to_date.strftime("%d/%m/%Y"),
                "adults": 2,
                "price_to": row["lowestPrice"] + 50,
            }

            response = requests.get(url=flight_search_end_point, params=parameters, headers=self.headers)
            flights_data = response.json()["data"]
            # print(f"flights data: {flights_data}")
            if flights_data:
                flight = flights_data[0]
                flight_data = FlightData(ORIGIN_CITY, ORIGIN_CITY_CODE,
                                         row["city"], row["iataCode"],
                                         from_date, to_date,
                                         flight["price"])
                available_flights.append(flight_data)

        return available_flights


    # def all_flights_available(self, iata_and_price: list) -> list:
    #     """Return a list of FlightData objects."""
    #
    #     def dates() -> list:
    #         """return a list of all the dates from today to six months ahead."""
    #
    #         def daterange(date1, date2):
    #             for n in range(int((date2 - date1).days) + 1):
    #                 yield date1 + timedelta(n)
    #
    #         current_year = date.today().year
    #         current_month = date.today().month
    #         current_day = date.today().day
    #
    #         # Get the month and the year after six months.
    #         if current_month + 6 > 12:
    #             end_month = current_month - 6
    #             end_year = current_year + 1
    #         else:
    #             end_month = current_month + 6
    #             end_year = current_year
    #
    #         start_dt = date(current_year, current_month, current_day)
    #         end_dt = date(end_year, end_month, current_day)
    #         six_months_dates = []
    #         for dt in daterange(start_dt, end_dt):
    #             six_months_dates.append(dt.strftime("%Y-%m-%d"))
    #
    #         return six_months_dates
    #
    #     # Get all the dates from today to six months ahead.
    #     all_dates = dates()
    #
    #     # Find whether there are flights that are lower than the lowest price.
    #     available_flights = []
    #     for destination in iata_and_price:
    #         for check_date in all_dates:
    #             try:
    #                 response = self.amadeus.analytics.itinerary_price_metrics.get(originIataCode=ORIGIN_CITY,
    #                                                                               destinationIataCode=destination[0],
    #                                                                               departureDate=check_date)
    #                 time.sleep(5)
    #                 print(response.data)
    #                 try:
    #                     available_lowest_price = float(response.data["data"][0]["priceMetrics"][0]["amount"])
    #                 except:
    #                     pass
    #                 else:
    #                     if available_lowest_price < destination[1]:
    #                         flight = FlightData(ORIGIN_CITY, destination[0], date, available_lowest_price)
    #                         available_flights.append(flight)
    #             except ResponseError as error:
    #                 raise error
    #     return available_flights



        # get_token_end_point = "https://test.api.amadeus.com/v1/security/oauth2/token"
        # headers = {
        #     "content-type": "application/x-www-form-urlencoded"
        # }
        # token_parameters = {
        #     "client_id": API_KEY,
        #     "client_secret": API_SECRET,
        #     "grant_type": "client_credentials"
        # }
        # response = requests.post(url=get_token_end_point, json=token_parameters, headers=headers)
        # print(response.raise_for_status())
        # data = response.json()
        # print(data)
