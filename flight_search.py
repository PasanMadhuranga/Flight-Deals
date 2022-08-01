import time

from amadeus import Client, ResponseError
from datetime import timedelta, date
from flight_data import FlightData

ORIGIN_CITY = "LON"


class FlightSearch:
    def __init__(self, amadeus_client, ):
        self.amadeus = amadeus_client

    def all_flights_available(self, iata_and_price: list) -> list:
        """Return a list of FlightData objects."""

        def dates() -> list:
            """return a list of all the dates from today to six months ahead."""

            def daterange(date1, date2):
                for n in range(int((date2 - date1).days) + 1):
                    yield date1 + timedelta(n)

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

            start_dt = date(current_year, current_month, current_day)
            end_dt = date(end_year, end_month, current_day)
            six_months_dates = []
            for dt in daterange(start_dt, end_dt):
                six_months_dates.append(dt.strftime("%Y-%m-%d"))

            return six_months_dates

        # Get all the dates from today to six months ahead.
        all_dates = dates()

        # Find whether there are flights that are lower than the lowest price.
        available_flights = []
        for destination in iata_and_price:
            # for check_date in all_dates:
                    try:
                        response = self.amadeus.shopping.flight_dates.get(origin='MAD', destination='MUC')
                        print(response.data)
                    except ResponseError as error:
                        raise error

                    # try:
                    #     available_lowest_price = float(response.data["data"][0]["priceMetrics"][0]["amount"])
                    # except:
                    #     pass
                    # else:
                    #     if available_lowest_price < destination[1]:
                    #         flight = FlightData(ORIGIN_CITY, destination[0], date, available_lowest_price)
                    #         available_flights.append(flight)
        return available_flights



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
