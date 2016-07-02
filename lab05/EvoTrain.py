from copy import deepcopy

from lab02.Neuron import Neuron


class EvoTrain(Neuron):

    def __init__(self, n, iterations, sigma, learning_set, excepted_response):
        super().__init__(n)
        self.iterations = iterations
        self.sigma = sigma
        self.x = Neuron(n)
        self.err_to_draw = []
        self.learning_set = learning_set
        self.excepted_response = excepted_response

    def evolve(self):
        self.err_to_draw = self.iterations * [0]
        for i in range(self.iterations):
            y = deepcopy(self.x)
            y.mutate(self.sigma)

            if self.get_err(self.x, i) > self.get_err(y, i):
                for j in range(len(y.w)):
                    self.x.w[j] = y.w[j]

    def get_err(self, neuron, step):
        y = []
        e = []
        s = 0

        for i, lset in enumerate(self.learning_set):
            y.append(neuron.feed(lset))
            temp_eq = y[i] - self.excepted_response[i]
            e.append(temp_eq**2)
            s += e[i]

        err = s/len(self.learning_set)
        print("Error: {0}".format(err))
        temp = self.err_to_draw[step]

        if temp == 0:
            self.err_to_draw[step] = err

        return err

if __name__ == "__main__":
    file = open("water.data")
    data = file.read()
    file.close()

    data = [row.split(',') for row in data.split("\n")]
    learning_set = [[float(c) for c in row[:-1]] for row in data]
    excepted_response = [float(row[-1]) for row in data]

    et = EvoTrain(4, 200, 0.01, learning_set, excepted_response)
    et.evolve()

    import matplotlib.pyplot as plt
    plt.plot(et.err_to_draw)
    plt.ylabel('some numbers')
    plt.show()
