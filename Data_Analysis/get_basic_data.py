import pandas as pd
from tkinter import filedialog, Tk
import os
from functools import reduce

from utils import get_stats, get_count, get_sum, get_max, get_min


#show all columns
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', None)

root=Tk()
root.withdraw()
directory= filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory to get all files:')

#column to group by:
category='Carrier_index'

index=1
global_stats=pd.DataFrame()


#calculate stats for each year and put it into a globbal table:
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file = pd.read_csv(os.path.join(directory, filename))
        yearly_stats = file['ARR_DELAY'].groupby(file[category]).apply(get_stats).unstack()
        yearly_stats = yearly_stats.sort_values(category)
        index=index+1
        print(index)
        if(index==1):
            global_stats=yearly_stats
        else:
            frames = [global_stats, yearly_stats]
            global_stats = pd.concat(frames)

#calculate global stats from global table


global_stats[category] = global_stats.index

global_count=global_stats['count'].groupby(global_stats[category]).apply(get_count)
global_max=global_stats['max'].groupby(global_stats[category]).apply(get_max)
global_min=global_stats['min'].groupby(global_stats[category]).apply(get_min)
global_sum=global_stats['sum'].groupby(global_stats[category]).apply(get_sum)


tables=[global_count.to_frame(), global_max.to_frame(), global_min.to_frame(),global_sum.to_frame()]

df_final = reduce(lambda left,right: pd.merge(left,right,on=category), tables)
df_final["mean"]=df_final["sum"]/df_final["count"]


print(df_final)

to_save='D:\studia\SEMESTR 7\inzynierka\Data\Analysed\Airlines.csv'
pd.DataFrame.to_csv(df_final,to_save)