from math import pi, cos


class EvaluationFunctionA:

    def apply(self, genotype):
        A = 10
        n = 2
        res = n*A
        for i in range(n):
            x = genotype[i]
            r = x**2 - A * cos(2 * pi * x)
            res += r
        return res
