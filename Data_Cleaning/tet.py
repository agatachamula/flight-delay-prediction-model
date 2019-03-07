import pandas as pd
from tkinter import filedialog, Tk
import os
from functools import reduce



#show all columns
pd.set_option('display.max_row', 10)
pd.set_option('display.max_columns', None)

root=Tk()
root.withdraw()
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')


global_stats=pd.DataFrame()
value="G4"
index=2002



#calculate stats for each year and put it into a globbal table:
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename))

        print(file.isnull())

        print(index)
        index = index + 1
