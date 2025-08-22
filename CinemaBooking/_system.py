from _cinema import Cinema
from _show import Show
from _booking import Booking


class CinemaSystem:
    def __init__(self):
        self.cinemas = {}
        self.shows = {}
        self.bookings = {}
        self.next_show_id = 1
        self.next_booking_id = 1

    def registerShow(self, cinema_name, movie_name, date_time, price, capacity):
        if cinema_name not in self.cinemas:
            self.cinemas[cinema_name] = Cinema(cinema_name)
        show_id = self.next_show_id
        self.next_show_id += 1
        show = Show(show_id, cinema_name, movie_name, date_time, price, capacity)
        self.cinemas[cinema_name].add_show(show)
        self.shows[show_id] = show
        return show_id

    def update_price(self, show_id, new_price):
        if show_id not in self.shows:
            raise Exception("Invalid show id")
        self.shows[show_id].price = new_price

    def start_show(self, show_id):
        if show_id not in self.shows:
            raise Exception("Invalid show id")
        self.shows[show_id].start()

    def end_show(self, show_id):
        if show_id not in self.shows:
            raise Exception("Invalid show id")
        self.shows[show_id].end()

    def order_ticket(self, movie_name, date_time, num_tickets):
        # Find matching shows
        candidate_shows = [
            show
            for show in self.shows.values()
            if show.movie_name == movie_name
            and show.date_time == date_time
            and not show.ended
        ]
        if not candidate_shows:
            return None, "No such show available"

        
        candidate_shows = [
            s for s in candidate_shows if s.remaining_seats >= num_tickets
        ]
        if not candidate_shows:
            return None, "Booking not possible. Reason: Booking Unavailable"

        
        cheapest_show = min(candidate_shows, key=lambda s: s.price)
        print(
            f"Booking assigned to {cheapest_show.cinema_name} at price {cheapest_show.price}"
        )

        total_amount, error = cheapest_show.book_tickets(num_tickets)
        if error:
            return None, f"Booking not possible. Reason: {error}"

        booking_id = self.next_booking_id
        self.next_booking_id += 1

        booking = Booking(booking_id, cheapest_show, num_tickets, total_amount)
        self.bookings[booking_id] = booking
        self.cinemas[cheapest_show.cinema_name].update_revenue(total_amount)

        return (
            booking_id,
            f"{num_tickets} tickets booked with total bill: {total_amount}",
        )

    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            return "Invalid booking id"
        booking = self.bookings[booking_id]
        refund = booking.cancel()
        if refund > 0:
            self.cinemas[booking.show.cinema_name].update_revenue(-refund)
        return f"Booking cancelled. Refund: {refund}"

    def print_system_stats(self):
        for cinema in self.cinemas.values():
            print(f"{cinema.name}, Revenue: {int(cinema.revenue)}")
