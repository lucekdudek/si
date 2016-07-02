from random import uniform


class Neuron:

    def __init__(self, n):
        self.w = []
        for i in range(n):
            self.w.append(uniform(-1.0, 1.0))

    def feed(self, x):
        result = 0
        for w_el, x_el in zip(self.w, x):
            result += w_el * x_el
        return result

    def learn(self, number_of_epos, learn_set, d, theta):
        for epo in range(number_of_epos):
            for learn_el, d_el in zip(learn_set, d):
                feed_res = self.feed(learn_el)
                e = d_el - feed_res
                delta_w = [theta*e*_ for _ in learn_el]
                self.w = [_ + __ for _, __ in zip(self.w, delta_w)]

    def update_weight(self, el, learning_rate):
        for i in range(len(self.w)):
            self.w[i] = (el[i] - self.w[i]) * learning_rate

if __name__ == "__main__":
    n = Neuron(12)
    x_ucz = [
        12 * [-1],
        12 * [1]
    ]
    d_oczek = [-1, 1]
    n.learn(500, x_ucz, d_oczek, 0.05)

    print(n.feed(12 * [1]))
