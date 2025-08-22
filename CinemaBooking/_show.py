import threading


class Show:
    def __init__(self, show_id, cinema_name, movie_name, date_time, price, capacity):
        self.show_id = show_id
        self.cinema_name = cinema_name
        self.movie_name = movie_name
        self.date_time = date_time
        self.price = price
        self.capacity = capacity
        self.remaining_seats = capacity
        self.started = False
        self.ended = False
        self.lock = threading.Lock()

    def start(self):
        if self.started:
            raise Exception("Show already started.")
        self.started = True

    def end(self):
        if not self.started:
            raise Exception("Show has not started yet.")
        if self.ended:
            raise Exception("Show already ended.")
        self.ended = True

    def book_tickets(self, num_tickets):
        with self.lock:
            if self.started:
                return None, "Show Already Started"
            if num_tickets > self.remaining_seats:
                return None, "No Seats Available"
            self.remaining_seats -= num_tickets
            return num_tickets * self.price, None

    def cancel_tickets(self, num_tickets):
        with self.lock:
            if not self.started:
                self.remaining_seats += num_tickets
