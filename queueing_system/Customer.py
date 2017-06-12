
class Customer(object):
    def __init__(self, time, arrival, departure):
        self.t_arrival = time + arrival
        self.t_departure = self.t_arrival + departure
