from numpy.random import poisson

class Customer(object):
    def __init__(self):
        pass

class Customer_no_queue(Customer):
    def __init__(self, time, m_arrive, m_service):
        self.t_arrival = time + poisson(m_arrive)
        self.t_departure = self.t_arrival + poisson(m_service)
        self.t_next = self.t_arrival

    def get_next_event_time(self, time):
        if time < self.t_arrival:
            self.t_next = self.t_arrival
        elif time < self.t_departure:
            self.t_next = self.t_departure
        else:
            self.t_next = -1
