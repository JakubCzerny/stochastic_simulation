import random
from Customer import Customer_no_queue

class Arrival_process_no_queue(object):
    def __init__(self, n, m_arrive, m_service, to_be_served):
        self.served = 0
        self.dropped = 0

        self.n = n
        self.m_service = m_service
        self.m_arrive = m_arrive
        self.to_be_served = to_be_served

        self.time = 0
        self.init_process()

    def init_process(self):
        # self.customers = [Customer(i, self.m_arrive) for i in range(self.to_be_served)]
        # self.customers.sort(key=lambda x: x.t_arrival)
        customer = Customer_no_queue(self.time, self.m_arrive, self.m_service)
        self.customers = [customer]

    def simulate(self):
        while self.served < self.to_be_served:
            self.time += 1

            for customer in self.customers:
                if customer.t_next < self.time:
                    self.customers.remove(customer)
                    self.served += 1

            if len(self.customers) < self.n:
                customer = Customer_no_queue(self.time, self.m_arrive, self.m_service)
                self.customers.append(customer)
            else:
                self.dropped += 1

            self.customers.sort(key=lambda x: x.get_next_event_time(self.time))

        print "Served: ",self.served, ' skipped: ',self.dropped

#
# class Arrival_process_renewal(object):
#     def __init__(self, n, m_arrive, m_service, to_be_served):
#         self.served = 0
#         self.dropped = 0
#
#         self.n = n
#         self.m_service = m_service
#         self.m_arrive = m_arrive
#         self.to_be_served = to_be_served
#
#         self.time = 0
#         self.init_process()
#
#     def init_process(self):
#         customer = Customer(self.time, self.m_arrive, self.m_service)
#         self.customers = [customer]
#
#     def simulate(self):
#         while self.served < self.to_be_served:
#             print "Served: ",self.served, ' skipped: ',self.dropped
#             self.time += 1
#
#             for customer in self.customers:
#                 if customer.t_next < self.time:
#                     self.customers.remove(customer)
#                     self.served += 1
#
#             if len(self.customers) < self.n:
#                 customer = Customer(self.time, self.m_arrive, self.m_service)
#                 self.customers.append(customer)
#             else:
#                 self.dropped += 1
#
#             self.customers.sort(key=lambda x: x.get_next_event_time(self.time))
