import os
import pandas as pd
import glob
import csv
import numpy as np
import pandas as pd


path = os.getcwd()
file = os.path.isfile('{}/allsongcompare.csv'.format(path))
if file:
	os.remove('{}/allsongcompare.csv'.format(path))
csv_list = glob.glob('*.csv') 
print(u'total %s csv files'% len(csv_list))
print(u'processing............')
#print(os.getcwd())
df_list = [] 
for filename in csv_list: 
    df_list.append(pd.read_csv(filename)) 
full_df = pd.concat(df_list) 
full_df.to_csv('allsongcompare.csv', index=False) 
print("finshed!")
