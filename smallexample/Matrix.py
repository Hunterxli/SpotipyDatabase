import os
import pandas as pd
import csv
import numpy as np
import pandas as pd

def Calavg():
	data = pd.read_csv('keywordcal/allsongcompare.csv')
	#print(data)
	#print(data.the_first_song[0])
	i = 0
	song1 = ""
	word1 = ""
	song2 = ""
	word2 = ""
	result = []
	calculation = 0
	avg = 0
	k = 0
	#while(i < len(data)):
	while(k < 11):
		song1 = data.the_first_song[i]
		word1 = data.word1[i]
		song2 = data.the_second_song[i]
		word2 = data.word2[i]
		#print(data.result[i])
		result.append(data.result[i])
		#print(result)
		if(data.the_second_song[i] != data.the_second_song[i + 1]):
			#print(result)
			for item in result:
				#print(item)
				calculation += float(item)
				#avg = calculation / (i + 1)
			#print(avg)
			print("{} and {}: {}".format(song1, song2, calculation))
			print("\n")
			k = k + 1
			calculation = 0
			result = []
			
		i = i + 1
		
def BuildMatirx():
	data = pd.read_csv('keywordcal/allsongcompare.csv')
	
	

Calavg()