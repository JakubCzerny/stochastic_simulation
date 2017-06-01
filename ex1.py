from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

a = 5
c = 1
M = 16
x0= 3
n = 1000
bins = 10

generator = LCG(a,c,M)
x = generator.simulate(x0,n)

hist, edges = np.histogram(x, bins=bins)
plt.bar(range(bins), hist, width=0.9)
plt.title("own implentation of LCG")
plt.show()
