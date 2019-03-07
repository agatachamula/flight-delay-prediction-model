import pandas as pd
from tkinter import filedialog, Tk
import os

#select file:

#first we will join all data for one year

#display all 14 columns:
pd.set_option('display.max_columns', None)

root=Tk()
root.withdraw()
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')

joined=pd.DataFrame()


file_number=1
for filename in os.listdir(directory):
    if filename.endswith(".csv"):

        file1 = pd.read_csv(os.path.join(directory, filename))
        if file_number==1:
            joined=file1
        if file_number!=1:
            frames = [joined, file1]
            joined=pd.concat(frames)
        print(file_number)
        file_number=file_number+1


to_save=directory+'\joined.csv'
pd.DataFrame.to_csv(joined,to_save, index=False)
print("finished")


