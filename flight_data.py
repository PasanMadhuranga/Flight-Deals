class FlightData:
    def __init__(self, origin_city, origin_city_code, destination_city, destination_city_code, from_date, to_date, price):
        self.origin_city = origin_city
        self.origin_city_code = origin_city_code
        self.destination_city_code = destination_city_code
        self.destination_city = destination_city
        self.from_date = from_date
        self.to_date = to_date
        self.price = price
