from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


class FlightDeals:
    def __init__(self):
        self.get_notified()

    def get_notified(self):
        """Send an email about lowest flight deals."""
        data_manager = DataManager()
        flight_search = FlightSearch()

        # Add IATA codes to the google sheet.
        data_manager.add_IATA_codes()
        # get a list of FlightData objects that are lower than the lowest price.
        available_flights_objects = flight_search.all_flights_available(data_manager.get_rows())

        # Send an email about flight deals.
        notification_manager = NotificationManager(available_flights_objects)
        notification_manager.send_notifications()


if __name__ == "__main__":
    flight_deals = FlightDeals()
