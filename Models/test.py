import pandas as pd
adver = pd.read_csv("2018.csv", usecols=[0,1, 2, 3, 4,5,6,7,8,9,10,11,12,14])
adver.head()
X, y = adver.iloc[:, :-1], adver.iloc[:, -1]

import sklearn.model_selection as ms
X_train, X_test, Y_train, Y_test = ms.train_test_split(X, y, test_size=0.25, random_state=42)


from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, Y_train)

y_pred=logisticRegr.predict(X_test)



from sklearn.metrics import classification_report
print(classification_report(Y_test, y_pred))




import coremltools
input_features = ["QUARTER","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","ORIGIN_STATE_FIPS","DEST_STATE_FIPS","CRS_DEP_TIME","CRS_ARR_TIME","CRS_ELAPSED_TIME",
                  "DISTANCE","Destination","Carrier_index","Origin"]
output_feature = "ARR_DELAY"

model = coremltools.converters.sklearn.convert(logisticRegr, input_features, output_feature)
model.save("logistic_model.mlmodel")