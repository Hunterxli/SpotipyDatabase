import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


num = 1
songName = []
songRelease = []
songArtist = []
def FindOne():
	data = pd.read_csv('user%s_songname.csv' %(num))
	i = 0
	while(i < len(data)):
		songName.append(data.song_name[i])
		songRelease.append(data.song_release[i])
		songArtist.append(data.song_artist[i])
		i = i + 1
	#print(songName)
	
def FindAll():
	k = 0
	t = 0
	count = 0
	while(k < len(songName)):
		name = songName[k]
		while(t < len(songName)):
			if(songName[t] != name):
				t = t + 1
			else:
				songName.pop(t)
				songRelease.pop(t)
				songArtist.pop(t)
				t = t + 1
				count = count + 1
		k = k + 1
	print(songName)
	print(count)
	

while(num < 101):
	FindOne()
	num = num + 1
FindAll()
s = 0
csvFile = open("allsongname.csv", "w", newline='')
fileHeader = ["song_name", "song_release", "song_artist"]
writer = csv.writer(csvFile)
writer.writerow(fileHeader)
while(s < len(songName)):
	d = [songName[s], songRelease[s], songArtist[s]]
	writer.writerow(d)
	s = s + 1
csvFile.close()