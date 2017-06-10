from __future__ import division
from discrete_distribution import geometric, crude, rejection, alias
import numpy as np

n = 10000
p = 0.5
x = geometric(p,n,True)

p = np.array([7/48, 5/48, 1/8, 1/16, 1/4, 5/16])
x = crude(p, n, True)
x = rejection(p,n,True)
x = alias(p,n,True)
