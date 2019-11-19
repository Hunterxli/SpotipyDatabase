import os
import pandas as pd
import csv
import numpy as np
import pandas as pd
from decimal import localcontext

def Buildmatrix():
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
	#while(i < len(data)):
	while(i < 587):
		song1 = data.the_first_song[i]
		word1 = data.word1[i]
		song2 = data.the_second_song[i]
		word2 = data.word2[i]
		#print(data.result[i])
		result.append(data.result[i])
		#print(result)
		if(data.the_second_song[i] == data.the_second_song[i + 1]):
			i = i + 1
		else:
			for item in result:
				calculation += float(item)
		print("{} and {}: {}".format(song1, song2, calculation))
		calculation = 0
		print("\n")
		i = i + 1
		
	
	

Buildmatrix()