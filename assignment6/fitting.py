import data
import sys
import glob
import sklearn
import pandas as pd

from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


def fitKNN(filename, feature1, feature2):
    # df = data.read_csv(filename)
    # df = df.drop(columns=["diabetes"])


    sets = data.make_sets(filename)


    training_set = sets[0]
    validation_set = sets[1]

    training_set = training_set.drop(columns=["diabetes"])
    validation_set = validation_set.drop(columns=["diabetes"])

    Y_train = training_set[feature2].values #Bare feature
    X_train = training_set.drop(columns=[feature1]) #Hele

    Y_valid = validation_set[feature2].values #Feature
    X_valid = validation_set.drop(columns=[feature1]) #Hele

    # print(df)
    # x1 = training_set.drop(columns=[feature])
    # y1 = validation_set[feature].values


    # X_train, X_valid, Y_train, Y_valid = train_test_split(x1, y1, test_size=0.30, random_state=1)


    # print(X_train)
    # print(Y_train)

    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, Y_train)
    pred_target = knn.predict(X_valid)
    # score = metrics.accuracy_score(Y_valid, pred_target)
    score = knn.score(X_valid, Y_valid)

    print("Score: %.2f%%" % (score*100.0))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        lstFiles = glob.glob(sys.argv[1])
    if all(lstFiles):
        print("Found all files :)\n")
        fitKNN(sys.argv[1], 'mass', 'glucose')
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
