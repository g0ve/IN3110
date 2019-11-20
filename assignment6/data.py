import sys
import glob
import matplotlib.pyplot as plt
import pandas as pd

def main(filename):
    # make_scatter(diabetes, "mass", "glucose")
    # make_scatter(diabetes, "glucose", "pregnant")
    diabetes = read_csv(filename)
    make_scatter(diabetes, "insulin", "triceps")

def read_csv(filename):
    diabetes = pd.read_csv(filename, sep=',')
    diabetes = diabetes.dropna()
    # print(diabetes)

    return diabetes

def make_sets(filename):
    diabetes = read_csv(filename)

    diabetes_copy = diabetes.copy()
    training_set = diabetes_copy.sample(frac=0.8, random_state=0)
    # print(training_set)
    validation_set = diabetes_copy.drop(training_set.index)
    # print(validation_set)

    return training_set, validation_set

def make_scatter(dataFrame, space1, space2):
    neg = dataFrame[dataFrame["diabetes"] == "neg"]
    pos = dataFrame[dataFrame["diabetes"] == "pos"]

    data = (space1, space2)
    colors = ("red", "green")
    groups = ("neg", "pos")

    fig, ax = plt.subplots(figsize = (20, 50))
    ax.scatter(neg[space1], neg[space2], zorder=1, alpha=1, c='red', s=20, label = "neg")
    ax.scatter(pos[space1], pos[space2], zorder=1, alpha=1, c='green', s=20, label = "pos")
    plt.title("Diabetes")
    plt.xlabel(space1)
    plt.ylabel(space2)
    plt.legend(loc=2, title="Diabetes", fontsize='small', fancybox=True, shadow=True, facecolor="grey")
    plt.show()
    # for data, colors, groups in zip(data, colors, groups):
    #     x, y = data
    # ax.scatter(x, y, zorder=1, alpha=1, c=colors, s=30, label=groups)

    # ax.set_title('Diabetes')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        lstFiles = glob.glob(sys.argv[1])
    if all(lstFiles):
        print("Found all files :)\n")
        main(sys.argv[1])
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
