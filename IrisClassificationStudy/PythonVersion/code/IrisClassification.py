import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from LogisticRegression import LogisticRegression
from Perceptron import Perceptron
from Adaline import Adaline
from Plot import Plot

class IrisClassification:
    def __init__(self):
        pass

    def fit(self):

        # READ THE DATASET
        data_path = "../dataset/iris.data"
        iris_df = pd.read_csv(data_path, sep=",", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

        # CONVERT DO NUMBER CATEGORY
        name_x_cat = {"Iris-setosa" : 0, "Iris-versicolor": 1, "Iris-virginica":2}
        iris_df["species"] = iris_df["species"].map(name_x_cat)


        X = iris_df.iloc[:, :-1]
        Y = iris_df.iloc[:, -1]

        ss = StandardScaler()
        # ss.fit(X)

        # X_std = ss.transform(X)
        # X_train, X_test, Y_train, Y_test = train_test_split(X_std, Y, test_size = 0.3, random_state = 45)

        # X_train_bin = X_train[(Y_train == 0) | (Y_train == 1)]
        # Y_train_bin = Y_train[(Y_train == 0) | (Y_train == 1)]
        #
        # X_test_bin = X_test[(Y_test == 0) | (Y_test == 1)]
        # Y_test_bin = Y_test[(Y_test == 0) | (Y_test == 1)]
        #
        # lr = LogisticRegression()
        # lr.fit(X_train_bin, Y_train_bin)
        #
        # y_pred = lr.predict(X_test_bin)

        # print((y_pred == Y_test_bin).sum() / len(Y_test_bin))

        # plot = Plot()
        #
        # y_ada = Y.iloc[0:100]
        # x_ada = X.iloc[0:100, [0,2]]
        #
        # X_train_ada, X_test_ada, Y_train_ada, Y_test_ada = train_test_split(x_ada, y_ada, test_size=0.3, random_state=45)
        #
        # ada = Adaline()
        # ada.fit(X_train_ada, Y_train_ada)
        #
        # y_pred = ada.predict(X_test_ada)
        #
        # print((y_pred == Y_test_ada).sum() / len(Y_test_ada))
        #
        # x_combined_std = np.vstack((X_train_ada, X_test_ada))
        # y_combined = np.hstack((Y_train_ada.values.ravel(), Y_test_ada.values.ravel()))
        #
        # plot.plotDecisionRegions(x_combined_std, y_combined, ada)

        # percep = Perceptron(iter_num=1)
        # percep.fit(X_train, Y_train)

        # x_bin = X.iloc[:100, [0,2]]
        # y_bin = Y.iloc[:100]

        x = [ [ 1.14177101,  0.99770792 ],
              [ 0.04542025,  1.06708956 ],
              [-1.20755205, -0.87559625 ],
              [ 0.51528486,  0.85894465 ],
              [-0.11120129, -0.80621461 ],
              [ 0.51528486,  0.72018138 ],
              [-0.42444437, -1.01435952 ],
              [-0.73768744, -0.87559625 ],
              [ 0.98514947,  1.27523447 ],
              [ 0.20204178,  1.1364712  ],
              [-0.5810659 , -0.66745134 ],
              [ 2.39474331,  1.27523447 ],
              [ 1.76825716,  1.20585283 ],
              [ 0.35866332,  1.1364712  ],
              [ 0.35866332,  0.92832629 ],
              [-0.42444437, -0.94497788 ],
              [-0.5810659 , -0.94497788 ],
              [-1.36417359, -1.29188606 ],
              [ 0.04542025,  0.65079974 ],
              [ 0.98514947,  0.78956302 ],
              [-1.52079513, -1.08374115 ],
              [-0.26782283, -0.94497788 ],
              [-1.36417359, -1.01435952 ],
              [ 0.35866332,  0.44265484 ],
              [ 2.23812177,  1.41399774 ],
              [-0.11120129, -1.08374115 ],
              [ 1.61163562,  1.20585283 ],
              [ 0.04542025,  0.78956302 ],
              [ 0.20204178,  0.51203647 ],
              [-0.42444437,  0.72018138 ],
              [-1.8340382 , -1.22250442 ],
              [-0.73768744, -1.01435952 ],
              [ 0.82852793,  1.55276101 ],
              [-0.73768744, -1.08374115 ],
              [-1.05093052, -0.87559625 ],
              [-1.67741667, -1.08374115 ],
              [-1.36417359, -1.01435952 ],
              [ 1.92487869,  1.48337938 ],
              [ 0.20204178,  0.92832629 ],
              [ 1.92487869,  1.27523447 ],
              [-0.73768744,  0.30389157 ],
              [-0.11120129, -0.94497788 ],
              [ 0.04542025, -1.08374115 ],
              [ 0.20204178,  0.85894465 ],
              [ 1.29839254,  1.27523447 ],
              [-0.5810659 ,  0.09574666 ],
              [ 0.98514947,  1.20585283 ],
              [-0.5810659 , -1.01435952 ],
              [ 0.04542025,  0.58141811 ],
              [-1.05093052, -0.66745134 ],
              [-0.89430898, -0.94497788 ],
              [-1.05093052, -1.01435952 ],
              [ 1.29839254,  1.06708956 ],
              [-1.67741667, -1.01435952 ],
              [-0.5810659 , -0.87559625 ],
              [ 1.29839254,  1.41399774 ],
              [-0.89430898,  0.30389157 ],
              [ 0.04542025,  0.78956302 ],
              [ 0.51528486, -1.15312279 ],
              [ 1.92487869,  1.06708956 ],
              [ 0.35866332, -0.94497788 ],
              [ 1.14177101,  1.1364712  ],
              [-0.73768744, -1.15312279 ],
              [ 0.82852793,  1.1364712  ],
              [ 0.6719064 ,  0.92832629 ],
              [ 0.35866332,  0.92832629 ],
              [-0.42444437, -0.94497788 ],
              [-1.36417359, -0.94497788 ],
              [-1.05093052, -0.87559625 ],
              [ 1.76825716,  1.06708956 ] ];

        y_bin = [ 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1 ]

        y = np.where(y_bin == 0, -1, 1)

        # ss.fit(x_bin)
        # X_std = ss.transform(x_bin)


        # print(x)
        # X_train, X_test, Y_train, Y_test = train_test_split(X_std, y, test_size = 0.3, random_state = 45)


        # print(Y_train)
        ada = Adaline(alpha=0.01, n_iter=10)
        ada.fit(pd.DataFrame(x), y)

        # print(ada.costs)
