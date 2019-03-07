import pandas as pd
from tkinter import Tk, filedialog
import os

#5,6,7,8,9,10,11
#show all columns
pd.set_option('display.max_columns', None)

#load directory with dictionaries:
root = Tk()
root.withdraw()
directory_of_dictionaries= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory of dictioniaries:')

#load all dictionaries:
flag=1
for filename in os.listdir(directory_of_dictionaries):
    if filename.endswith(".csv"):
        if(flag==1):
            airports = pd.read_csv(os.path.join(directory_of_dictionaries, filename))
        if(flag==2):
            carriers = pd.read_csv(os.path.join(directory_of_dictionaries, filename))
        if(flag==3):
            pass
        print(flag)
        flag=flag+1



#select directory with data:
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')

flag=1
#for each file do the join
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename))

        """
        #rename columns to be joined on carrier:
        carriers.rename(columns={'OP_UNIQUE_CARRIER': 'Carrier'}, inplace=True)
        file.rename(columns={'OP_UNIQUE_CARRIER': 'Carrier'}, inplace=True)
        #merge on the Carrier:
        file=pd.DataFrame.merge(file,carriers, on='Carrier')
        #drop the columns we don't need anymore:
        file=file.drop(columns=['Carrier', 'Name'])

        # rename columns to be joined on origin:
        airports.rename(columns={'Airport': 'Origin'}, inplace=True)
        file.rename(columns={'ORIGIN': 'Origin'}, inplace=True)
        # merge on the Origin:
        file = pd.DataFrame.merge(file, airports, on='Origin')
        # drop the columns we don't need anymore:
        file=file.drop(columns=['Origin'])
        file.rename(columns={'Airport_index': 'Origin'}, inplace=True)

        """
        # rename columns to be joined on destination:
        airports.rename(columns={'Airport': 'Destination'}, inplace=True)
        file.rename(columns={'DEST': 'Destination'}, inplace=True)
        # merge on the Destination:
        file = pd.DataFrame.merge(file, airports, on='Destination')
        # drop the columns we don't need anymore:
        file=file.drop(columns=['Destination'])
        file.rename(columns={'Airport_index': 'Destination'}, inplace=True)


    # save the table to csv again:
    file.to_csv(os.path.join(directory, filename), index=False)

    # print progress
    print(flag)
    flag = flag + 1


