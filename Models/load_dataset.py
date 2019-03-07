import pandas as pd
from sklearn import model_selection
import os
import numpy

def get_dataset(ratio):

    directory = "D:/studia/SEMESTR 7/inzynierka/Data/test"

    X_columns = [1,2,3]
    Y_columns=[4]

    X=[]
    Y=[]
    index=1

    # calculate stats for each year and put it into a globbal table:
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):

            #read X values from file

            fileX = pd.read_csv(os.path.join(directory, filename), usecols=X_columns)
            fileY = pd.read_csv(os.path.join(directory, filename), usecols=Y_columns)

            if (index == 1):
                X=fileX
                Y=fileY
            else:
                framesX = [X, fileX]
                X = pd.concat(framesX)

                framesY = [Y, fileY]
                Y = pd.concat(framesY)
            print(index)
            index=index+1


    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=ratio)
    print(type(X_train.as_matrix()))

    return X_train.as_matrix(), X_test.as_matrix(), Y_train.as_matrix(), Y_test.as_matrix()

