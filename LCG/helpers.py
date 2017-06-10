from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare, chi2


def extract_increasing_intervals(x):
    tmp = [[x[0]]]

    for i in range(1,len(x)):
        if x[i] >= x[i-1]:
            tmp[-1].append(x[i])
        else:
            tmp.append([x[i]])

    return tmp

def up_down_test(x, alpha):
    n = len(x)
    runs = [len(ival) for ival in extract_increasing_intervals(x)]
    A = np.array([
        [4529.4, 9044.9, 13568, 18091, 22615, 27892],
        [9044.9, 18097, 27139, 36187, 45234, 55789],
        [13568, 27139, 40721, 54281, 67852, 83685],
        [18091, 36187, 54281, 72414, 90470, 111580],
        [22615, 45234, 67852, 90470, 113262, 139476],
        [27892, 55789, 83685, 111580, 139476, 172860],
    ])
    B = np.array([1/6, 5/24, 11/120, 19/720, 29/5040, 1/840])
    R = np.array([0]*6)

    for val in runs:
        if val < 2:
            R[0] += 1
        elif val < 3:
            R[1] += 1
        elif val < 4:
            R[2] += 1
        elif val < 5:
            R[3] += 1
        elif val < 6:
            R[4] += 1
        else:
            R[5] += 1

    tmp = R-n*B
    Z = (1 / (n-6)) * np.matmul(np.matmul(tmp,A),tmp)
    crit = chi2.isf(alpha, 6)

    print "Up/down test:\nCritical value:",crit, " Z:",Z,'\n'


def chi2_test(x, alpha, bins, name=False, save=False):
    n = len(x)
    hist, _ = np.histogram(x, bins=bins)
    crit = chi2.isf(alpha, bins-1)
    expected = [n/bins]*bins
    T = sum(np.divide(np.power(hist - expected, 2),expected))

    print "Chi2:\nCritical value:",crit, " t-stat:", T,'\n'

    if name:
        title = name
        if name != 'python':
            title='own LCG'
        plt.figure()
        plt.bar(range(bins), hist, width=0.9)
        plt.title(title)

        if save:
            plt.savefig('figures/'+name+'.png')


def pair_plots(x, color='r'):
    plt.figure()
    plt.scatter(x[:-1],x[1:], s=10, c=color)
