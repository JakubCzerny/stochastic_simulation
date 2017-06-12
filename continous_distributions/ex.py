from continous_distributions import exponential, box_muller, pareto, normal
import matplotlib.pyplot as plt

rate = 4
n = 10000

def plot_CIs_series(x,horizonal):
    plt.figure()
    plt.plot(range(len(x[0])), x[0])
    plt.plot(range(len(x[0])), x[1])
    plt.axhline(horizonal,0,len(x[0]))

def plot_CIs_lines(x,horizonal):
    plt.figure()
    [plt.plot((i,i), (mean_ci[0][i],mean_ci[1][i])) for i in range(len(mean_ci[0]))]
    plt.axhline(horizonal,0,len(mean_ci[0]))

mean_ci, var_ci = normal(10, alpha=0.05, reps=100, plot=False)
plot_CIs_series(mean_ci,0)
plot_CIs_series(var_ci,1)
plt.show()


# mean_ci, var_ci = normal(1000, alpha=0.05, reps=1, plot=False)
# box_muller(n,True)
# exponential(rate, n,True)

# beta = 1
# pareto(beta, k=2.05, n=n, plot=True)
# pareto(beta, k=2.5, n=n, plot=True)
# pareto(beta, k=3, n=n, plot=True)
# pareto(beta, k=4, n=n, plot=True)
