# I am completely and utterly lost










import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        self.weights = [np.random.standard_normal(s) for s in weight_shapes]
        self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]

    def predict(self, a):
        for w,b in zip(self.weights,self.biases):
            a = self.activation(np.matmul(w,a) + b)
        return a
    def print_accuracy(self, images, labels):
        predictions = self.predict(images)
        # I'll make a list comprehension
        num_correct = sum([np.argmax(a) == np.argmax(b) for a,b in zip(predictions, labels)])
        print('{0}/{1} accuracy: {2}%'.format(num_correct,len(images), (num_correct/len(images))*100))

    @staticmethod
    def activation(x):
        return 1/(1+np.exp(-x))

layer_sizes = (784,5,10)
x = np.ones((layer_sizes[0],1))  # our input vector x has size of the 0th index of layer_sizes 9which is the size of first layer, 1)
MyNetwork = NeuralNetwork(layer_sizes)
prediction = MyNetwork.predict(training_images)
print(prediction.shape)

MyNetwork.print_accuracy(training_images, training_labels)









# I tried some searching some websites to help me out and I can't seem to grasp what is going on.
# Below code from:
# http://neuralnetworksanddeeplearning.com/chap1.html

import random

# Third-party libraries
import numpy as np

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):

        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in xrange(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print "Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test)
            else:
                print "Epoch {0} complete".format(j)

    def update_mini_batch(self, mini_batch, eta):

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in xrange(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):

        return (output_activations-y)

#### Miscellaneous functions
def sigmoid(z):

    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):

    return sigmoid(z)*(1-sigmoid(z))


import mnist_loader
training_data, validation_data, test_data = \
mnist_loader.load_data_wrapper()


import network
net = network.Network([784, 30, 10])


