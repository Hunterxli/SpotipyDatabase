import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time

num = 11
while(num < 101):
	data = pd.read_csv('user%s.csv' %(num),header=None)
	data.columns = ['user_id','song_id','listen_time']
	#print(data)
	#print(len(data))
	songId = []
	songName = []
	songRelease = []
	songArtist = []
	songListen = []
	#print(data.song_id[0])
	i = 0
	k = len(data)
	while i < k:
		songId.append(data.song_id[i])
		songListen.append(data.listen_time[i])
		i = i + 1
	print(songId)
	print(songListen)


	song = pd.read_csv('D:\\finalproject\\SpotipyDatabase-master\\SpotipyDatabase-master\\song_data.csv')
	#print(song)
	t = 0#song id
	l = len(songId)
	#print(l)
	while t < l:
		id = songId[t]
		t1 = len(song)
		s1 = 0#song title
		while s1 < t1:
			start = time.perf_counter()#calculate the running time
			if(song.song_id[s1] == id):
				songName.append(song.title[s1])
				songRelease.append(song.release[s1])
				songArtist.append(song.artist_name[s1])
				print(song.title[s1])
				print("the %s song" %(t+1))
				print("it's %s in the song list" %(s1))
				end = time.perf_counter()#calculate the running time
				run_time = end - start
				print("the running time: %s" %(run_time))
				print("\n")
				break
			else:
				s1 = s1 + 1
		t = t + 1
	print(songName)

	fileHeader = ["song_name", "song_release", "song_artist", "listen_time"]
	s = 0
	csvFile = open("user%s_songname.csv" %(num), "w", newline='')
	writer = csv.writer(csvFile)
	writer.writerow(fileHeader)
	while(s < l):
		d = [songName[s], songRelease[s], songArtist[s], songListen[s]]
		writer.writerow(d)
		s = s + 1
	csvFile.close()
	num = num + 1
	
	


# file=open('data1-1.csv','w')
# for items in data:
	# for item in items:
		# file.write(item)
		# file.write(",")
	# file.write("\n")
# file.close()