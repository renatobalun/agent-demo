from llama_index.core.tools.tool_spec.base import BaseToolSpec

class BookingReservationAvailabilityToolSpec(BaseToolSpec):
    """Booking reservation availability tool spec."""

    spec_functions = ["booking_reservation_availabiliy"]

    def booking_reservation_availabiliy(self):
        """A tool for reservations, booking and availability of rooms."""

        booking = {
            "answer": "To get precise information on prices and room availability, please input the desired date of arrival and departure with the use of a button.",
            "important": [
                "Never use dates when displaying this answer.",
                "Highlight that the user should use the button."
            ]
        }
        
        return booking
