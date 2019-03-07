import pandas as pd
sample = pd.read_csv("2017.csv", usecols=[0,1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14])

sample=pd.DataFrame.sample(sample, n=10000)


print(sample.head(5))

sample.to_csv("sample.csv", index=False)