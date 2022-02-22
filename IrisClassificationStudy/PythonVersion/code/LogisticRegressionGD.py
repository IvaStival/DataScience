import pandas as pd
import numpy as np

class LogisticRegressionGD:
    def __init__(self, eta=0.01, n_iter=10, seed=45):
        self.eta = eta
        self.n_iter = n_iter
        self.seed = seed

        self.w = []
        self.cost = []

    def fit(self, X, Y):
        rgen = np.random.RandomState(self.seed)
        self.w = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        for i in range(self.n_iter):
            y_line = self.net_input(X)
            output = self.activation(y_line)
            error = (Y - output)

            self.updateWeights(X, error)

            cost = (-Y.dot(np.log(output)) - (1 - Y).dot(np.log(1 - output)))
            self.cost.append(cost)
        print(self.cost)

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.5, 1, 0)

    def activation(self, y_line):
        return 1.0 / (1.0 + np.exp(-np.clip(y_line, -250, 250)))

    def updateWeights(self, X, error):
        self.w[0] += self.eta * error.sum()
        self.w[1:] += self.eta * X.T.dot(error)
