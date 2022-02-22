import numpy as np
import pandas as pd


class AdalineSGD:

    def __init__(self, eta=0.01, n_iter=1, random_seed=45, shuffle=True):
        self.eta = eta
        self.n_iter = n_iter
        self.random_seed = random_seed
        self.shuffle = shuffle
        self.w = []
        self.initialized_w= False
        self.cost = []

    def fit(self, X, Y):
        self.initializeWeights(X.shape[1])
        # self.shuffleData(np.array(X),np.array(Y))
        for i in range(self.n_iter):
            cost_temp = []

            if self.shuffle:
                X_s, Y_s = self.shuffleData(X, Y)

            # print(X_s[0])
            for xi, target in zip(X_s, Y_s):
                # print(xi)
                cost_temp.append(self.updateWeights(xi, target))

            avg_cost = sum(cost_temp) / len(Y_s)
            self.cost.append(avg_cost)

        print(self.cost)
        return self

    def partialFit(self, X, Y):
        if not self.initialized_w:
            self.initializeWeights(X.shape[1])
        if Y.ravel().shape[0] > 1:
            for xi, target in zip(X,Y):
                self.updateWeghts(xi,target)

        else:
            self.updateWeghts(X,Y)

        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def activation(self, y_line):
        return y_line

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >=0.0, 1, -1 )

    def updateWeights(self, X, Y):
        output = self.activation(self.net_input(X))
        error = (Y - output)


        self.w[1:] += self.eta * X.dot(error)
        self.w[0] += self.eta * error.sum()
        cost = 0.5 * error ** 2

        return cost


    def initializeWeights(self, var_size):
        self.rgen = np.random.RandomState(self.random_seed)
        self.w = self.rgen.normal(loc=0.0, scale=0.01, size=1+var_size)

        self.initialized_w = True

    def shuffleData(self, X, Y):
        r = self.rgen.permutation(len(Y))

        return X[r], Y[r]
