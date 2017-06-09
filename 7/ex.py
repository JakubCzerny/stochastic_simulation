from simulated_annealing import SA_coordinates, SA_distances
import random
import numpy as np


def get_coordinates(D):
    M = np.empty(shape=D.shape)

    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            M[i,j] = np.divide(np.power(D[1,j],2) + np.power(D[i,1],2) + np.power(D[i,j],2), 2)

    return M


# ================================================== COORDINATES ============================================================
# x = [(1,2), (5,1), (8,3), (1,9), (12,7), (41,26), (50,30), (60,25), (55,27), (30,30)]
x = [(random.random(),random.random()) for i in range(20)]
t0 = 400
max_time = 30
SA = SA_coordinates(t0, x, max_time)
print "Initial route length: ", SA.distance

SA.simulate()
print "Final route length: ", SA.distance
print 'Number of iterations: ', SA.iterations
print 'Final temperature: ', SA.t
SA.display('initial')
SA.display('final')
# ===========================================================================================================================



# ================================================== DISTANCES ============================================================
# D = np.loadtxt('distances.txt', delimiter="\t", dtype='int')
# M = get_coordinates(D)
# t0 = 700
# max_time = 30
#
# SA = SA_distances(t0, M, max_time)
# print "Initial route length: ", SA.distance
#
# SA.simulate()
# print "Final route length: ", SA.distance
# print 'Number of iterations: ', SA.iterations
# SA.display('initial')
# SA.display('final')
# ===========================================================================================================================
