class LCG(object):
    def __init__(self, a, c, M):
        self.a = a
        self.c = c
        self.M = M

    def simulate(self, x0, n):
        x = [x0]
        for i in range(n):
            x.append((self.a*x[-1]+self.c) % self.M)

        return x[1:]
