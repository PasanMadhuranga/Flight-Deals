import requests
from amadeus import Client, ResponseError

TEQUILA_API_KEY = "HcHDQ-0lzJRWUQn3_M3DLwQeSYuBePfb"


class DataManager:
    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_API_KEY
        }

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
            city_codes = []
            for city_name in cities:
                city_name = {
                    "term": city_name
                }
                iata_end_point = "https://tequila-api.kiwi.com/locations/query"
                city_code_response = requests.get(url=iata_end_point, params=city_name, headers=self.headers)
                city_code = city_code_response.json()["locations"][0]["code"]
                city_codes.append(city_code)

            return city_codes

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

    def get_rows(self) -> list:
        """Return all the rows in the spread sheet as a list of dictionaries."""
        get_rows_endpoint = "https://api.sheety.co/d9b6498affde17f134d087d65eb61e1d/flightDeals/prices"
        response = requests.get(url=get_rows_endpoint)
        rows = response.json()["prices"]
        return rows
        # return [(row["iataCode"], row["lowestPrice"]) for row in rows]