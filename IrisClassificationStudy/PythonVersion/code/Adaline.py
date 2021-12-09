import numpy as np

class Adaline:

    def __init__(self, alpha=0.02, n_iter=100, random_state=45):
        self.alpha = alpha
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, Y):

        rgen = np.random.RandomState(self.random_state)
        # self.w = rgen.normal(loc=0.0, scale=0.1, size = 1 + X.shape[1])

        self.w = [0.01, 0.01, 0.01]

        self.costs = []

        for i in range(self.n_iter):
            y_line = self.net_input(X)
            output = self.activation(y_line)
            errors = (Y - output)

            self.w[1:] += self.alpha * X.T.dot(errors)
            self.w[0] += self.alpha * errors.sum()

            # print(self.w[1:])

            cost = (errors**2).sum() / 2.0

            self.costs.append(cost)

        print(self.costs)


    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def sigmoid(self, z):
        return 1. / (1. + np.exp(np.clip(z, -250, 250)))

    def activation(self, X):
        return X

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)
