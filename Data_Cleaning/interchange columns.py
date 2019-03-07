import pandas as pd
from tkinter import Tk, filedialog
import os


root = Tk()
root.withdraw()
# select directory with data:
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')

flag=1
#for each file do the join
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        frame = pd.read_csv(os.path.join(directory, filename))
        frame = frame[["QUARTER", "MONTH", "DAY_OF_MONTH", "DAY_OF_WEEK", "ORIGIN_STATE_FIPS", "DEST_STATE_FIPS", "CRS_DEP_TIME",
                       "CRS_ARR_TIME", "CRS_ELAPSED_TIME", "DISTANCE", "Destination", "Carrier_index", "Origin", "ARR_DELAY"]]

    # save the table to csv again:
    frame.to_csv(os.path.join(directory, filename), index=False)

    # print progress
    print(flag)
    flag = flag + 1