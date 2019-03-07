import pandas as pd
from tkinter import Tk, filedialog
import os

#display all rows with airline code KH

#show all columns
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', None)

root=Tk()
root.withdraw()
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')

number_of_rows=0
number_after_drop=0
flag=1

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename))
        number_of_rows=number_of_rows + file.shape[0]
        print(flag)
        file=file.dropna(axis=0)
        number_after_drop=number_after_drop+file.shape[0]
        flag=flag+1
        file.to_csv(os.path.join(directory, filename), index=False)
       # print(file[file.isnull().any(axis=1)])





print(number_of_rows)
print(number_after_drop)
print(number_after_drop/number_of_rows)



#105948479
#104048483
#0.9820667930494783

#8382853
#8169782
#0.9745825198175371

#106206870
#104182203
#0.980936572182195




