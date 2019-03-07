import pandas as pd
from tkinter import Tk, filedialog

#5,6,7,8,9,10,11
#show all columns
pd.set_option('display.max_columns', None)

#select file
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir="/", title="Select data file:")

#load the file as dataframe without last and first column:
cols_to_use = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
file= pd.read_csv(file_path, usecols= cols_to_use)


#show state of the table
print(file.head(5))

#save with the columns removed:
file.to_csv(file_path,index=False)


