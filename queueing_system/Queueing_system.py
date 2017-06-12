from __future__ import division
import random
import numpy as np
from Customer import Customer

class Arrival_process(object):
    def __init__(self, n, arrival, service, to_be_served):
        self.served = 0
        self.blocked = 0

        self.arrival = arrival
        self.service = service
        self.n = n
        self.to_be_served = to_be_served

        self.time = 0
        self.init_process()

    def init_process(self):
        customer = Customer(self.time, self.arrival.get_value(), self.service.get_value())
        self.customers = [customer]

    def simulate(self):
        while self.served < self.to_be_served:
            self.time += 1 / self.interarrival.mean

            for customer in self.customers:
                if customer.t_next < self.time:
                    self.customers.remove(customer)
                    self.served += 1

            if len(self.customers) < self.n:
                customer = Customer(self.time, self.arrival.get_value(), self.service.get_value())
                self.customers.append(customer)
            else:
                self.blocked += 1

            self.customers.sort(key=lambda x: x.get_next_event_time(self.time))

        print "Served: ",self.served, ' skipped: ',self.blocked


class Renewal_process(object):
    def __init__(self, n, interarrival, service, to_be_served):
        self.served = 0
        self.blocked = 0

        self.interarrival = interarrival
        self.service = service
        self.n = n
        self.to_be_served = to_be_served

        self.time = 0
        self.init_process()

    def init_process(self):
        customer = Customer(self.time, self.interarrival.get_value(), self.service.get_value())
        self.last_arrival = customer.t_arrival
        self.customers = [customer]

    def simulate(self):
        while self.served < self.to_be_served:
            self.time += 1/self.interarrival.mean

            for customer in self.customers:
                if customer.t_departure < self.time:
                    self.customers.remove(customer)
                    self.served += 1

            customer = Customer(self.time, self.arrival.get_value(), self.service.get_value())
            if len(self.customers) < self.n:
                self.customers.append(customer)
            else:
                self.blocked += 1
