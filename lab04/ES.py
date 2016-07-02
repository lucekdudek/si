from copy import deepcopy

from lab04.Speci import Speci
from lab04.EvaluationFunctionA import EvaluationFunctionA


class ES:

    def __init__(self, iterations, sigma):
        self.ev_fnc = EvaluationFunctionA()
        self.iterations = iterations
        self.sigma = sigma
        self.solution = Speci(10, -10, 10)
        self.x = Speci(10, -10, 10)
        self.y = Speci(10, -10, 10)
        self.success = 0
        self.last_sigma_inc = 0

    def evolve(self):
        for i in range(self.iterations):
            self.x.evaluate(self.ev_fnc)

            self.y = deepcopy(self.x)
            self.y.mutate(self.sigma)
            self.y.evaluate(self.ev_fnc)

            if self.y.fit < self.x.fit:
                self.x = deepcopy(self.y)
                self.success += 1

            self.update_sigma(i)

        self.solution = self.x

    def update_sigma(self, i):
        cd = 0.82
        ci = 1.0
        check_step = self.iterations/100
        if i % check_step == 0:
            if self.success > 20:
                self.sigma *= cd
            elif self.success < 20:
                self.sigma *= ci
            self.success = 0

if __name__ == "__main__":
    es = ES(100000, 0.8)
    es.evolve()
    print(es.solution.fit)
