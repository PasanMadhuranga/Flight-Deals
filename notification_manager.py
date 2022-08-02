import smtplib
from flight_data import FlightData
MY_EMAIL = "pasan7989@yahoo.com"
MY_PASSWORD = "vkyojatvkjghoqkm"

class NotificationManager:
    def __init__(self, available_flight_details):
        self.available_flight_details = available_flight_details

    def send_notifications(self):
        """Create a message to send."""
        message = ""
        for flight in self.available_flight_details:
            message += f"Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_city_code} to {flight.destination_city}-{flight.destination_city_code}, from {flight.from_date} to {flight.to_date}.\n\n "
        self.send_an_email(message)

    def send_an_email(self, message):
        """Send an email about the low price alert."""
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"Subject:Low Price Alert!\n\n{message}")
