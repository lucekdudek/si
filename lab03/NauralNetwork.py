from lab02.Neuron import Neuron


class NeuralNetwork:

    def __init__(self, population, size):
        self.size = size
        self.network = []
        for i in range(size):
            self.network.append(Neuron(population))

    def train(self, learning_set, epoch, learning_rate):
        for i in range(epoch):
            for el in learning_set:
                s = self.neural_feed(el)
                id_winner = self.find_winner_neuron(s)
                self.learn_winner(id_winner, el, learning_rate)

    def neural_feed(self, feed_set):
        result = []
        for neuron in self.network:
            result.append(neuron.feed(feed_set))
        return result

    def find_winner_neuron(self, feed_res):
        index = None
        result = -10
        for i, neuron in enumerate(self.network):
            f = neuron.feed(feed_res)
            if f >= result:
                result = f
                index = i
        return index

    def learn_winner(self, id, set, rate):
        self.network[id].update_weight(set, rate)

    def neural_respond(self, set):
        s = self.neural_feed(set)
        id = self.find_winner_neuron(s)
        respond = self.size*[0]
        respond[id] = 1
        return respond

if __name__ == "__main__":

    file = open("iris.data")
    data = file.read()
    file.close()

    data = [row.split(',') for row in data.split("\n")]

    training_data = [[float(c) for c in row[:-1]] for row in data if len(row) > 1]

    test_set = [[5.1, 3.5, 1.4, 0.2],
                [7.0, 3.2, 4.7, 1.4],
                [6.3, 3.3, 6.0, 2.5]
                ]
    network = NeuralNetwork(4, 3)
    network.train(training_data, 500, 0.1)

    print(network.neural_respond(test_set[0]))
    print(network.neural_respond(test_set[1]))
    print(network.neural_respond(test_set[2]))
