import pandas as pd
adver = pd.read_csv("sample.csv", usecols=[0,1, 2, 3, 4,5,6,7,8,9,10,11,12,15])
adver.head()

#adver=pd.DataFrame.sample(adver,n=40000)

X, y = adver.iloc[:, :-1], adver.iloc[:, -1]

import sklearn.model_selection as ms
X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(X_train, y_train)


y_pred=clf.predict(X_test)



from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test,y_pred))


"""
import coremltools
input_features = ["QUARTER","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","ORIGIN_STATE_FIPS","DEST_STATE_FIPS","CRS_DEP_TIME","CRS_ARR_TIME","CRS_ELAPSED_TIME",
                  "DISTANCE","Destination","Carrier_index","Origin"]
output_feature = "ARR_DELAY"

model = coremltools.converters.sklearn.convert(clf, input_features, output_feature)
model.save("tree.mlmodel")
"""