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


def normal(mean, var, n, plot=False):
    std = math.sqrt(var)
    x = [(mean + std * random.random()) for i in range(n)]

    if plot:
        plot_cdf(x, 'normal', int(n/10))

    mean_samples = np.mean(x)
    print 'Mean: ', mean_samples," true mean:",mean

    variance_samples = np.var(x)
    print 'Variance: ', variance_samples, " true variance:",var,'\n'

    return x


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


    mean_samples = np.mean(x)
    mean = 0
    var = 1
    alpha = 0.05
    print "Alpha: ", str(alpha)

    conf_int = stats.t.interval(alpha, n-1, mean_samples, 1)
    print 'Mean: ',conf_int[0],'<',mean_samples,'<',conf_int[1]," true mean:",mean

    variance_samples = np.var(x)
    conf_int = stats.t.interval(alpha, n-1, variance_samples, 1)
    print 'Variance: ', conf_int[0],'<',variance_samples,'<',conf_int[1], " true variance:",var,'\n'

    return [x,y]

def pareto(beta, k, n, plot=False):
    x = np.array([beta*(math.pow(random.random(), (-1/k))) for i in range(n)])
    x = x[np.where(x>beta)]

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
