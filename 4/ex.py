from Queueing_system import Arrival_process_no_queue#, Arrival_process_renewal

systems = [Arrival_process_no_queue(10, 1, 8, 10000).simulate() for i in range(10)]
