from random import uniform, gauss


class Speci:

    def __init__(self, n, min, max):
        self.fit = None
        self.genotype = []
        for i in range(n):
            self.genotype.append(uniform(min, max))

    def evaluate(self, fnc):
        self.fit = fnc.apply(self.genotype)

    def mutate(self, sigma):
        self.genotype = [e + gauss(0, sigma) for e in self.genotype]
