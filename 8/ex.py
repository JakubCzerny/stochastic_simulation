from bootstrap import bootstrap, estimate_p, get_median, get_mean
import numpy as np
from scipy.stats import pareto
import matplotlib.pyplot as plt

# Ex 13 / chapter 7
# x = [56,101,78,67,93,87,64,72,80,69]
# rep = 100
# b = bootstrap(x,rep)
# estimate_p(x, b, -5, 5)

beta = 1
k = 1.05
N = 200
alpha = 1.05

x = [pareto.pdf(r, alpha, loc=0, scale=beta) for r in np.arange(N)]
rep = 100
b = bootstrap(x,rep)

median, median_var = get_median(x,b)
mean, mean_var = get_mean(x,b)

print 'Mean:',mean,'+/-',mean_var,"\nMedian:",median,'+/-',median_var

'''
Mean is much more affected by the outliers / values being placed far in the tail
The median is being skewed by 1 sample whereas the mean is affected by the actual value of the sample
'''
