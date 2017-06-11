from continous_distributions import exponential, box_muller, pareto, normal

rate = 4
n = 10000

mean_ci, var_ci = normal(10, alpha=0.05, reps=100, plot=False)
box_muller(n,True)
exponential(rate, n,True)

beta = 1
pareto(beta, k=2.05, n=n, plot=True)
pareto(beta, k=2.5, n=n, plot=True)
pareto(beta, k=3, n=n, plot=True)
pareto(beta, k=4, n=n, plot=True)
