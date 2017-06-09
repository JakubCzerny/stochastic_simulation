from integration import monte_carlo, antithetic_variables, control_variates, stratified_sampling
import math

def f_exp(x):
    return math.exp(x)

n = 100
alpha = 0.05
integral, var, conf_int = monte_carlo(n, f_exp, alpha=alpha)
print "[MONTE CARLO]:\n", conf_int[0],' < ', integral, ' < ', conf_int[1], '\nvariance: ', var,'\n'

integral, var, conf_int = antithetic_variables(n, f_exp, alpha=alpha)
print "[ANTITHETIC VARIABLES]:\n", conf_int[0],' < ', integral, ' < ', conf_int[1], '\nvariance: ', var,'\n'

integral, var, conf_int = control_variates(n, f_exp, alpha=alpha)
print "[CONTROL VARIATES]:\n", conf_int[0],' < ', integral, ' < ', conf_int[1], '\nvariance: ', var,'\n'

n = 10
integral, var, conf_int = stratified_sampling(n, f_exp, strata=10, alpha=alpha)
print "[STRATIFIED SAMPLING]:\n", conf_int[0],' < ', integral, ' < ', conf_int[1], '\nvariance: ', var,'\n'
