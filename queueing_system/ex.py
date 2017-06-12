from __future__ import division
from Queueing_system import Arrival_process, Renewal_process
from numpy.random import poisson, gamma, exponential
import numpy as np
import math
from scipy import stats

class Poisson:
    def __init__(self, rate):
        self.rate = rate
        self.mean = rate
    def get_value(self):
        return poisson(self.rate)

class Erlang:
    def __init__(self, p, rate):
        self.p = p
        self.rate = rate
        self.mean = p / rate
    def get_value(self):
        return gamma(self.p, 1/self.rate)

class Exponential:
    def __init__(self, rate):
        self.rate = rate
        self.mean = 1/rate
    def get_value(self):
        return exponential(1/self.rate)

tmp = []
class Hyper_Exponential:
    def __init__(self, probs, rates):
        self.probs = probs
        self.rates = rates
        self.mean = np.sum(np.array(probs)/np.array(rates))
    def get_value(self):
        exps = np.array([exponential(1/rate) for rate in self.rates])
        tmp.append(np.sum(exps*self.probs))
        return np.sum(exps*self.probs)

def generate_CI(x):
    mean = np.mean(x)
    var = np.var(x)
    alpha = 0.05
    ci = stats.t.interval(1-alpha, len(systems)-1, mean, math.sqrt(var))
    ci = [max(0,ci[0]),ci[1]]

    print "Blocked: ",ci[0],"<", mean,"<",ci[1],'\n'


# systems = [Arrival_process(10, Poisson(1), Poisson(8), 10000) for i in range(10)]
# [system.simulate() for system in systems]
# generate_CI([system.blocked for system in systems])
#
# systems = [Arrival_process(10, Poisson(1), Exponential(1/8), 10000) for i in range(10)]
# [system.simulate() for system in systems]
# generate_CI([system.blocked for system in systems])
#
# systems = [Renewal_process(10, Erlang(1,1), Exponential(1/8), 10000) for i in range(10)]
# [system.simulate() for system in systems]
# generate_CI([system.blocked for system in systems])

# systems = [Renewal_process(10, Hyper_Exponential([0.8, 0.2], [0.8333, 5.0]), Exponential(1/8), 10000) for i in range(10)]
# [system.simulate() for system in systems]
# generate_CI([system.blocked for system in systems])

systems = [Renewal_process(10, Hyper_Exponential([0.8, 0.2], [0.8333, 5.0]), Poisson(8), 10000) for i in range(10)]
[system.simulate() for system in systems]
generate_CI([system.blocked for system in systems])
