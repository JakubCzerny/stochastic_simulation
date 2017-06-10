from __future__ import division
import numpy as np
import random
import math
import matplotlib.pyplot as plt


def plot_cdf(x, bins=False):
    if not bins:
        bins = len(np.unique(x))

    plt.figure()
    hist, _ = np.histogram(x, bins=bins)
    plt.bar(range(bins), hist, width=0.9)
    plt.show()

def geometric(p,n,plot=False):
    x = []
    for i in range(n):
        u = random.random()
        x.append(math.floor(np.divide(math.log(u), math.log(1-p)) + 1))

    plot_cdf(x)

    return x


def crude(p,n,plot=False):
    x = []
    cdf = np.zeros(len(p)+1)
    for i in range(len(p)):
        cdf[i] = sum(p[:i])
    cdf[-1] = 1

    for i in range(n):
        u = random.random()
        x.append(np.where(u>cdf)[0].shape[0])

    plot_cdf(x)

    return x


def rejection(p,n,plot=False):
    x = []
    eps = 10**(-5)
    c = max(p) + eps

    while len(x) < n:
        r1 = 1+math.floor(len(p)*random.random())
        r2 = random.random()
        if r2 < p[int(r1)-1] / c:
            x.append(r1)

    plot_cdf(x)

    return x


def alias(p,n,plot=False):
    x = []
    eps = 10**(-5)
    c = max(p) + eps

    L = np.zeros((len(p)))
    F = len(p) * p
    G = np.array(np.where(F>=1))[0]
    S = np.array(np.where(F<=1))[0]

    while len(S) != 0:
        k = G[0]
        j = S[0]

        L[j] = k
        F[k] = F[k] - (1-F[j])

        if F[k] < 1 - eps:
            G = np.delete(G,0)
            S = np.append(S,k)
        S = np.delete(S,0)

    while len(x) < n:
        r1 = int(math.floor(len(p)*random.random()))
        r2 = random.random()

        if r2 < F[r1]:
            x.append(r1)
        else:
            x.append(L[r1])

    plot_cdf(x)

    return x
