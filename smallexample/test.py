import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

client_credentials_manager = SpotifyClientCredentials(client_id='3e909e4b4f194e66b3865f64d9b99b77', client_secret='8d8d2d9416e845a9bef9d46b9e21b583')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
	
data = pd.read_csv('user1.csv')
data.columns = ['user_id','song_id','listen_time']
print(data)
print(len(data))
songId = []
songName = []
songListen = []
print(data.song_id[0])
i = 0
k = len(data)
while i < k:
	songId.append(data.song_id[i])
	songListen.append(data.listen_time[i])
	i = i + 1
print(songId)
print(songListen)




song = pd.read_csv('D:\\final project\\The Echo Nest Taste Profile Subset\\song_data.csv')
print(song)
t = 0#song id
l = len(songId)
print(l)
while t < l:
	id = songId[t]
	t1 = len(song)
	s1 = 0#song title
	while s1 < t1:
		if(song.song_id[s1] == id):
			songName.append(song.title[s1])
			print(song.title[s1])
			s1 = s1 + 1
		else:
			s1 = s1 + 1
	t = t + 1
print(songName)

# file=open('data1-1.csv','w')
# for items in data:
	# for item in items:
		# file.write(item)
		# file.write(",")
	# file.write("\n")
# file.close()