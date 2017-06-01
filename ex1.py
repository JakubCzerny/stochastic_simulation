from __future__ import division
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare, chi2
from helpers import extract_increasing_intervals


'''
c = 19
M = 512

M = 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2
mod(a,p) = 1  ---> a = 1
'''


'''
c = 17
M = 1024

M = 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2
mod(a,p) = 1  ---> a = 1
'''

a = 1
c = 371
M = 1024
x0= 3
n = 10000
bins = 20

generator = LCG(a,c,M)
x = generator.simulate(x0,n)
unique = np.unique(x).shape[0]

hist, _ = np.histogram(x, bins=bins)
plt.bar(range(bins), hist, width=0.9)
plt.title("own implentation of LCG")
plt.savefig('figures/'+str(x0)+'_'+str(a)+'_'+str(c)+'_'+str(M)+'_'+str(bins)+'_'+str(unique)+'.png')


chisq,p = chisquare(list(hist),[n/bins]*bins)
print chisq, p

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
