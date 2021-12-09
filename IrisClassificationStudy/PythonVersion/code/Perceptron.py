import pandas as pd
import numpy as np



class Perceptron:
    def __init__(self, seed=45, eta=0.01, iter_num=10):

        self.seed = seed
        self.eta  = eta
        self.iter_num = iter_num

    def fit(self, X, Y):

        rgen = np.random.RandomState(self.seed)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        self.errors = []

        for _ in range(self.iter_num):
            error = 0
            for xi, target in zip(X, Y):
                update = self.eta * (target - self.predict(xi))
                print(self.predict(xi))
                print(xi)

                self.w_[1:] += update * xi
                self.w_[0]  += update

                error += int(update != 0.0)
            self.errors.append(error)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1 , -1)
