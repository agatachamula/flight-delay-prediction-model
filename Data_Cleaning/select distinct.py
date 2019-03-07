import pandas as pd
from tkinter import Tk, filedialog
import os
import numpy as np

#show all columns
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', None)

root=Tk()
root.withdraw()
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')

flag=1
my_values=[]
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename))
        unique=file.ORIGIN.unique()
        unique2 = file.DEST.unique()
        if flag==1:
            my_values=unique
        if flag!=1:
            my_values=np.append(my_values,unique)
        my_values=np.append(my_values,unique2)
        print(flag)
        flag=flag+1

#select unique from all unique from each year:
final_result=np.unique(my_values)

#transpose array to get one column matrix:
final_result=np.reshape(final_result,(len(final_result),1))

#make dataframe and save to csv with indexes:
columns_names=["AIRPORT"]
df=pd.DataFrame(final_result, columns=columns_names)
df.to_csv(os.path.join(directory, "Airport_list.csv"))

#print(to_save)




