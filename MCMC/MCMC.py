from __future__ import division
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare,chi2

def MCMC(i, arrival_rate, service_time, n=1000, warmup=1000):
    A = arrival_rate * service_time
    rvs = [random.randint(0,i)]
    lookup = [A ** j / math.factorial(j) for j in range(i+1)]

    for j in range(n+warmup):
        x = rvs[-1]
        y = random.randint(0,i)
        p = random.random()
        tmp = min(1, lookup[y] / lookup[x])

        if p < tmp:
            rvs.append(y)
        else:
            rvs.append(x)

    rvs = rvs[warmup:]
    hist, _ = np.histogram(rvs, bins=range(i+2))
    plt.bar(range(i+1), hist, width=0.9)

    prob = np.array(lookup) / np.sum(lookup)
    expected = (prob * n).astype(int)

    ind = np.where(expected==0)
    expected = np.delete(expected, ind)
    hist = np.delete(hist, ind)
    T = sum(np.divide(np.power(hist - expected, 2),expected))

    alpha = 0.05
    crit = chi2.isf(alpha, i-1)

    if T < crit:
        print "Hypothesis accepted: t_stat:",T,"<","critical value:",crit
    else:
        print "Hypothesis rejected: t_stat:",T,">","critical value:",crit

    plt.show()


def MCMC_joint(i, n=1000, warmup=1000):
    A1 = 4
    A2 = 4
    rvs = [random.randint(0,i)]
    lookup = [A ** j / math.factorial(j) for j in range(i+1)]

    for j in range(n+warmup):
        x = rvs[-1]
        y = random.randint(0,i)
        p = random.random()
        tmp = min(1, lookup[y] / lookup[x])

        if p < tmp:
            rvs.append(y)
        else:
            rvs.append(x)

    rvs = rvs[warmup:]
    hist, _ = np.histogram(rvs, bins=range(i+2))
    plt.bar(range(i+1), hist, width=0.9)

    prob = np.array(lookup) / np.sum(lookup)
    expected = (prob * n).astype(int)

    ind = np.where(expected==0)
    expected = np.delete(expected, ind)
    hist = np.delete(hist, ind)
    T = sum(np.divide(np.power(hist - expected, 2),expected))

    alpha = 0.05
    crit = chi2.isf(alpha, i-1)

    if T < crit:
        print "Hypothesis accepted: t_stat:",T,"<","critical value:",crit
    else:
        print "Hypothesis rejected: t_stat:",T,">","critical value:",crit

    plt.show()
