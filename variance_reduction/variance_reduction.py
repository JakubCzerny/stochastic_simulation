from __future__ import division
import random
import numpy as np
import scipy as sp
from scipy import stats
import math

def monte_carlo(n, f, alpha=0.05):
    rvs = [random.random() for i in range(n)]
    x  = [f(r) for r in rvs]
    x2 = [f(r)**2 for r in rvs]
    mean  = np.mean(x)
    var = np.mean(x2)-mean**2
    conf_int = stats.t.interval(1-alpha, n-1, mean, math.sqrt(var))

    return [mean, var, conf_int]


def antithetic_variables(n, f, alpha=0.05):
    rvs = [random.random() for i in range(n)]
    x = np.array([f(r) for r in rvs])
    Y = (x + math.e/x)/2
    mean  = np.mean(Y)
    var = np.mean(Y**2)-mean**2
    conf_int = stats.t.interval(1-alpha, n-1, mean, math.sqrt(var))

    return [mean, var, conf_int]


def control_variates(n, f, alpha=0.05):
    rvs = np.array([random.random() for i in range(n)])
    x = np.array([f(r) for r in rvs])
    cov = np.cov(x,rvs)[0,1]
    c = -cov / np.var(rvs)
    # c = -0.14086*12
    z = x + c*(rvs-0.5)

    mean = np.mean(z)
    var  = np.mean(z**2) - mean**2
    conf_int = stats.t.interval(1-alpha, n-1, mean, math.sqrt(var))

    return [mean, var, conf_int]


def stratified_sampling(n, f, strata, alpha=0.05):
    rvs = np.random.rand(n,strata)
    W = np.array([ sum(f(r/n + i/n)/n for i,r in enumerate(rvs[:,s])) for s in range(strata)])
    mean = np.mean(W, axis=0)
    var  = np.mean(W**2) - mean**2
    conf_int = stats.t.interval(1-alpha, n-1, mean, math.sqrt(var))

    return [mean, var, conf_int]
