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
songUser = []
def FindOne():
	data = pd.read_csv('user%s_songname.csv' %(num))
	i = 0
	while(i < len(data)):
		songName.append(data.song_name[i])
		songRelease.append(data.song_release[i])
		songArtist.append(data.song_artist[i])
		songUser.append(num)
		i = i + 1
	
	#print(songName[0])
	

while(num < 101):
	FindOne()
	num = num + 1
print(len(songName))
newlist = []
repName = []
for name in songName:
	if name not in newlist:
		newlist.append(name)
	else:
		repName.append(name)
songName = newlist
print(len(songName))
print(repName)
#print(songName[0])
s = 0
csvFile = open("allsongname.csv", "w", newline='', encoding='utf-8')
fileHeader = ["song_name", "song_release", "song_artist", "user"]
writer = csv.writer(csvFile)
writer.writerow(fileHeader)
while(s < len(songName)):
	d = [songName[s], songRelease[s], songArtist[s], songUser[s]]
	writer.writerow(d)
	s = s + 1
csvFile.close()