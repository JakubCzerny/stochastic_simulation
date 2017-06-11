from __future__ import division
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from scipy import stats

def plot_cdf(x, name="", bins=False):
    if not bins:
        bins = len(np.unique(x))

    plt.figure()
    hist, _ = np.histogram(x, bins=bins)
    plt.bar(range(bins), hist, width=0.9)
    plt.title(name)
    plt.show()


def exponential(rate,n,plot=False):
    x = [-math.log(random.random())/rate for i in range(n)]

    if plot:
        plot_cdf(x, 'exponential', int(n/10))

    return x


def normal(n, alpha=0.05, reps=1, plot=False):
    mean = 0
    var = 1

    ci_m = [0,0]
    ci_v = [0,0]

    for i in range(reps):
        x,_ = box_muller(n)
        mean_samples = np.mean(x)
        variance_samples = np.var(x)

        if plot:
            plot_cdf(x,'Normal',bins=int(n))

        ci = stats.t.interval(1-alpha, n-1, mean_samples, stats.sem(x))
        ci_m[0] += ci[0]
        ci_m[1] += ci[1]
        print 'Mean: ',ci[0],'<',mean_samples,'<',ci[1]," true mean:",mean

        numerator = (n-1) * variance_samples
        ci = [numerator / stats.chi2.isf(q=alpha/2, df=n-1), numerator / stats.chi2.isf(q=1-alpha/2, df=n-1)]

        ci_v[0] += ci[0]
        ci_v[1] += ci[1]
        print 'Variance: ', ci[0],'<',variance_samples,'<',ci[1], " true variance:",var,'\n'

    ci_m = np.array(ci_m) / reps
    ci_v = np.array(ci_v) / reps

    return [ci_m, ci_v]


def box_muller(n, plot=False):
    x = []
    y = []

    for i in range(n):
        phi = 2*math.pi*random.random()
        r = math.sqrt(-2*math.log(random.random()))

        x.append(r * math.cos(phi))
        y.append(r * math.sin(phi))

    if plot:
        plt.figure()
        plt.scatter(x,y,s=10, c='r')
        plt.show()

    return [x,y]

def pareto(beta, k, n, plot=False):
    x = [beta*(math.pow(random.random(), (-1/k))) for i in range(n)]

    if plot:
        name = '[Pareto] beta:',beta, ' k:',k
        plot_cdf(x, name, int(n/10))

    if k>1:
        mean = np.mean(x)
        mean_true = beta * k / (k-1)
        print 'Mean: ', mean," true mean:",mean_true

    if k>2:
        variance = np.var(x)
        variance_true = math.pow(beta,2) * k / (math.pow(k-1,2)*(k-2))
        print 'Variance: ', variance," true variance:",variance_true,'\n'

    return x
