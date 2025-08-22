class Cinema:
    def __init__(self, name):
        self.name = name
        self.shows = {}
        self.revenue = 0.0

    def add_show(self, show):
        self.shows[show.show_id] = show

    def update_revenue(self, amount):
        self.revenue += amount
