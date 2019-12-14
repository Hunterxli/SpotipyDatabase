import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import *

def Checkre():
	song1 = []
	song2 = []
	Cal_final = []
	new_list = []
	new_list2 = []
	final_list = []
	i = 0
	data = pd.read_csv('Final.csv')
	while(i < len(data)):
		song1.append(data.song1[i])
		song2.append(data.song2[i])
		Cal_final.append(data.Cal_final[i])
		i = i + 1
	k = 0
	j = 0
	new_list0 = column_stack((song1, song2, Cal_final))
	new_list = column_stack((song1, song2, Cal_final))
	new_list2 = column_stack((song2, song1, Cal_final))
	#print(new_list)
	#print(new_list2)
	#print("\n")
	while(k < len(new_list)):
		while(j < len(new_list2)):
			if((new_list[k] == new_list2[j]).all()):
				#print(k)
				new_list = np.delete(new_list,k,axis = 0)
				
			j = j + 1
		k = k + 1
	#print(new_list[2][0])
	song1 = []
	song2 = []
	Cal_final = []
	a = 0
	while(a < len(new_list)):
		song1.append(new_list[a][0])
		song2.append(new_list[a][1])
		Cal_final.append(new_list[a][2])
		a = a + 1
	# print(song1)
	# print(song2)
	# print(Cal_final)
	s = 0
	csvFile = open("Final_real.csv", "w", newline='', encoding='utf-8')
	fileHeader = ["song1", "song2", "Cal_final"]
	writer = csv.writer(csvFile)
	writer.writerow(fileHeader)
	while(s < len(song1)):
		d = [song1[s], song2[s], Cal_final[s]]
		writer.writerow(d)
		s = s + 1
	csvFile.close()
	print("Finish!")
				
				
				
Checkre()