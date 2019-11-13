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
print(u'total%s csv files'% len(csv_list))
print(u'processing............')
#print(os.getcwd())

for i in csv_list: 
	fr = open(i,'rb').read()
	with open('allsongcompare.csv','ab') as f: 
		f.write(fr)
print(u'finish！')
