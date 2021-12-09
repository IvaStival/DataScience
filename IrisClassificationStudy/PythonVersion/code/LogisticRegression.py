import numpy as np

class LogisticRegression:
    def __init__(self, alpha=0.03, n_iter=100, random_state=45):
        self.alpha = alpha
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, Y):
        rgen = np.random.RandomState(self.random_state)
        self.w = rgen.normal(loc=0.0, scale=0.1, size=1 + X.shape[1])

        self.costs = []

        for i in range(self.n_iter):
            calc_y = self.calculation(X)
            output = self.sigmoid(calc_y)

            errors = (Y - output)

            self.w[1:] += self.alpha * X.T.dot(errors)
            self.w[0]  += self.alpha * errors.sum()

            cost = (-Y.dot(np.log(output)) - ((1-Y).dot(np.log(1-output))))

            self.costs.append(cost)

    def cost(self, error):
        return (error ** 2)/2.0

    def calculation(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self, X):
        return np.where(self.calculation(X) >= 0.0, 1, 0)

    def sigmoid(self, z):
        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))
