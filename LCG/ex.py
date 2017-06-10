from __future__ import division
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt
from helpers import extract_increasing_intervals, up_down_test, chi2_test, pair_plots
import random

# Setup
a = 6364136223846793005
c = 1442695040888963407
M = 2**64
x0= random.randint(0,M)
n = 10000
bins = 20
alpha = 0.05

print "Own implementation of LCG\n"
x = LCG(a,c,M).simulate(x0,n)
chi2_test(x, alpha, bins, name=str(x0)+'_'+str(a)+'_'+str(c)+'_'+str(M)+'_'+str(bins)+'_')
up_down_test(x, alpha)
pair_plots(x,'b')

print "Mersenne Twister python\n"
x = [random.randint(0,M) for i in range(n)]
chi2_test(x, alpha, bins, name='python')
up_down_test(x, alpha)
pair_plots(x,'g')

plt.show()
