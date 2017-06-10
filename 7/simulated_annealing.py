from __future__ import division
import numpy as np
import math
import random
from scipy.spatial import distance
import matplotlib.pyplot as plt
import time
from copy import deepcopy

class SA_coordinates(object):
    def __init__(self, t0, x, max_time=5):
        self.t = t0
        self.max_time = max_time
        self.x = np.array(x)
        self.n = len(x)
        self.route = np.array([])
        self.iterations = 0
        self.init()


    def init(self):
        perm = np.random.permutation(np.arange(self.n))
        self.intial_route = self.x[perm]
        self.route = self.x[perm]
        dist = self.calc_dist(self.route)

        self.distance = dist
        self.distances = [dist]


    def calc_dist(self, x):
        dist = 0
        for i in range(self.n-1):
            dist += distance.euclidean(x[i],x[i+1])
        dist += distance.euclidean(x[0],x[-1])
        return dist


    def display(self, solution):
        if len(self.route.shape) is not 2:
            print 'The coordinates are not 2D'
        else:
            route = self.intial_route if solution=='initial' else self.route
            plt.figure()
            for i in range(self.n-1):
                plt.plot([route[i][0], route[i+1][0]],[route[i][1], route[i+1][1]])
            plt.plot([route[self.n-1][0], route[0][0]],[route[self.n-1][1], route[0][1]])


    def random_swap(self):
        x1 = random.randint(0,self.n-1)
        x2 = random.randint(0,self.n-1)

        while x1 == x2:
            x2 = random.randint(0,self.n-1)

        copy_route = deepcopy(self.route)
        tmp = deepcopy(self.route[x1])
        copy_route[x1] = copy_route[x2]
        copy_route[x2] = tmp

        distance = self.calc_dist(copy_route)
        self.distances.append(distance)
        diff = distance - self.distance

        if diff < 0:
            self.route = copy_route
            self.distance = distance
        else:
            prob = math.exp(-1/self.t*diff)
            r = random.random()

            if r < prob:
                self.route = copy_route
                self.distance = distance


    def update_t(self):
        self.t = self.t - 1/math.sqrt(1+self.iterations)


    def simulate(self):
        init_time = time.time()

        while ((time.time() - init_time) < self.max_time) and self.t > 0:
            # print "Current temp: ",self.t, ' distance:', self.distance
            self.random_swap()
            self.iterations += 1
            self.update_t()


class SA_distances(object):
    def __init__(self, t0, D, max_time=5):
        self.t = t0
        self.max_time = max_time
        self.D = D
        self.n = D.shape[0]
        self.route = np.array([])
        self.iterations = 0
        self.init()


    def init(self):
        x = np.random.permutation(np.arange(self.n))
        self.intial_route = x
        self.route = x
        dist = self.calc_dist(self.route)

        self.distance = dist
        self.distances = [dist]


    def calc_dist(self, x):
        dist = 0
        for i in range(self.n-1):
            dist += self.D[x[i],x[i+1]]
        return dist


    def display(self, solution):
        if len(self.route.shape) is not 2:
            print 'The coordinates are not 2D'
        else:
            route = self.intial_route if solution=='initial' else self.route
            plt.figure()
            for i in range(self.n-1):
                plt.plot([route[i][0], route[i+1][0]],[route[i][1], route[i+1][1]])
            plt.plot([route[self.n-1][0], route[0][0]],[route[self.n-1][1], route[0][1]])


    def random_swap(self):
        x1 = random.randint(0,self.n-1)
        x2 = random.randint(0,self.n-1)

        while x1 == x2:
            x2 = random.randint(0,self.n-1)

        copy_route = deepcopy(self.route)
        tmp = deepcopy(self.route[x1])
        copy_route[x1] = copy_route[x2]
        copy_route[x2] = tmp

        distance = self.calc_dist(copy_route)
        self.distances.append(distance)
        diff = distance - self.distance

        if diff < 0:
            self.route = copy_route
            self.distance = distance
        else:
            prob = math.exp(-1/self.t*diff)
            r = random.random()

            if r < prob:
                self.route = copy_route
                self.distance = distance


    def update_t(self):
        self.t = self.t - 1/math.sqrt(1+self.iterations)


    def simulate(self):
        init_time = time.time()

        while ((time.time() - init_time) < self.max_time) and self.t > 0:
            # print "Current temp: ",self.t, ' distance:', self.distance
            self.random_swap()
            self.iterations += 1
            self.update_t()
