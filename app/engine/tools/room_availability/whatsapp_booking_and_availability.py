from llama_index.core.tools.tool_spec.base import BaseToolSpec

class WhatsappBookingReservationAvailabilityToolSpec(BaseToolSpec):
    """Booking reservation availability tool spec."""

    spec_functions = ["booking_reservation_availabiliy"]

    def booking_reservation_availabiliy(self, sender_name:str = ""):
        """A tool for booking, reservations and availability of rooms."""
        
        return f"""{sender_name}, thank you for wanting to book a room with us! :)

        Feel free to reach out at any of the contacts: 
        - phone: +385 11 111 1111
        - email: info@grandhotel.com
        
        Please prepare the neccesarry information like how many guests are staying, arrival and departure dates and what room you would like to stay in.
        Looking forward to hosting you!
        If you need any more information feel free to ask.
        """
