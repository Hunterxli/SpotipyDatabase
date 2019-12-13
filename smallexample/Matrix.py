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
	
	cal2 = 0
	cal3 = 0
	final = 0
	
	song1list = []
	song2list = []
	cal1list = []#similarity
	cal2list = []#same artist
	cal3list = []#same user for the artist
	finlist = []
	
	avg = 0
	k = 0
	while(i < len(data)):
	#while(k < 11):
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
			#print("'{}' and '{}': {}".format(song1, song2, calculation))
			cal2, cal3 = Calartist(song1, song2) #check if two songs belong to same artist
			final = calculation + cal2 + cal3
			#print("final result: {}".format(final))
			print("'{}' and '{}': {}".format(song1, song2, final))
			#print("\n")
			song1list.append(song1)
			song2list.append(song2)
			cal1list.append(calculation)
			cal2list.append(cal2)
			cal3list.append(cal3)
			finlist.append(final)
			k = k + 1
			calculation = 0
			result = []
		i = i + 1
	# print(song1list)
	# print(song2list)
	# print(cal1list)
	# print(cal2list)
	# print(cal3list)
	s = 0
	csvFile = open("Fianl.csv", "w", newline='', encoding='utf-8')
	fileHeader = ["song1", "song2", "similarity", "Cal_artist", "Cal_user", "Cal_final"]
	writer = csv.writer(csvFile)
	writer.writerow(fileHeader)
	while(s < len(song1list)):
		d = [song1list[s], song2list[s], cal1list[s], cal2list[s], cal3list[s], finlist[s]]
		writer.writerow(d)
		s = s + 1
	csvFile.close()
		
		
def Calartist(s1, s2):
	data2 = pd.read_csv('allsongname.csv')
	k = 0
	artist1 = ""
	artist2 = ""
	calculation2 = 0
	calculation3 = 0
	user1 = ""
	user2 = ""
	while(k < len(data2)):
		if(data2.song_name[k] == s1):
			artist1 = data2.song_artist[k]		
			#print(artist1)
			k = k + 1
		elif(data2.song_name[k] == s2):
			artist2 = data2.song_artist[k]
			#print(artist2)
			k = k + 1
		else:
			k = k + 1
	#print("base on their artist calculation:")
	if(artist1 == artist2):
		calculation2 = 1
		#print("base on their artist calculation:{}".format(calculation2))
	#else:
		#print("base on their artist calculation:{}".format(calculation2))
		
	j = 0
	while(j < len(data2)):
		if(artist1 == data2.song_artist[j]):
			user1 = data2.user[j]
			j = j + 1
		elif(artist2 == data2.song_artist[j]):
			user2 = data2.user[j]
			j = j + 1
		else:
			j = j + 1
	if(user1 == user2):
		calculation3 = 1
		#print("base on the same user like this atrist:{}".format(calculation3))
	#else:
		#print("base on the same user like this atrist:{}".format(calculation3))
	return calculation2, calculation3


Calavg()