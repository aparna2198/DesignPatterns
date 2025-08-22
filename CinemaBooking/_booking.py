class Booking:
    def __init__(self, booking_id, show, num_tickets, total_amount):
        self.booking_id = booking_id
        self.show = show
        self.num_tickets = num_tickets
        self.total_amount = total_amount
        self.cancelled = False

    def cancel(self):
        if self.cancelled:
            return 0.0
        self.cancelled = True

        if not self.show.started:
            # Refund 50% before show start and release seats
            refund = 0.5 * self.total_amount
            self.show.cancel_tickets(self.num_tickets)
            return refund
        else:
            # After show started → no refund, seats not released
            return 0.0
