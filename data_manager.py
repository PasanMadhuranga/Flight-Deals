import requests
from amadeus import Client, ResponseError

class DataManager:
    def __init__(self, amadeus_client):
        self.amadeus = amadeus_client

    def add_IATA_codes(self):
        """Get all the city names from the sheet and get relevant IATA codes and update the 'ATA code' column"""

        def get_city_names() -> list:
            """Get all the city names from the sheet."""
            get_rows_endpoint = "https://api.sheety.co/d9b6498affde17f134d087d65eb61e1d/flightDeals/prices"
            response = requests.get(url=get_rows_endpoint)
            rows = response.json()["prices"]
            city_names = [row["city"] for row in rows]
            return city_names

        def get_IATA_codes(cities: list) -> list:
            """Get all the relevant iata codes for the given city names list."""
            iata_codes = []
            for city_name in cities:
                try:
                    response = self.amadeus.reference_data.locations.cities.get(keyword=city_name)
                    all_locations = response.data
                    try:
                        iata_code = all_locations[0]["iataCode"]
                        iata_codes.append(iata_code)
                    except KeyError:
                        for location in all_locations:
                            if location["name"] == city_name:
                                try:
                                    iata_codes.append(location["iataCode"])
                                    break
                                except KeyError:
                                    pass
                except ResponseError as error:
                    raise error
            return iata_codes

        def update_sheet(iata_codes: list):
            """Update the 'IATA code' column"""
            for index in range(len(iata_codes)):
                edit_row_end_point = f"https://api.sheety.co/d9b6498affde17f134d087d65eb61e1d/flightDeals/prices/{index + 2}"
                parameters = {
                    "price": {
                        "iataCode": iata_codes[index]
                    }
                }
                requests.put(url=edit_row_end_point, json=parameters)

        iata_codes = get_IATA_codes(get_city_names())
        update_sheet(iata_codes)



    def code_and_price(self) -> list:
        """Return a list of IATA code and the lowest price in a tuple"""
        get_rows_endpoint = "https://api.sheety.co/d9b6498affde17f134d087d65eb61e1d/flightDeals/prices"
        response = requests.get(url=get_rows_endpoint)
        rows = response.json()["prices"]
        return [(row["iataCode"], row["lowestPrice"]) for row in rows]