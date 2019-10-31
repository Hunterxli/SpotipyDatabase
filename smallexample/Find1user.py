import csv
import pandas as pd
import numpy as np
import os
from rake_nltk import Rake

num = 1
name = []
release = []
artist = []
listen = []
word = []
def Findwords():
	data = pd.read_csv('user%s_songname.csv' %(num))
	data.columns = ['song_name','song_release','song_artist', 'listen_time']
	i = 0
	while(i < len(data)):
		name.append(data.song_name[i])
		release.append(data.song_release[i])
		artist.append(data.song_artist[i])
		listen.append(data.listen_time[i])
		i = i + 1
	# print(name)
	# print(release)
	# print(artist)
	# print(listen)
	print(i)
	r = Rake()
	r.extract_keywords_from_text(name[0])
	keyword = r.get_ranked_phrases()
	word.append(keyword)
	print(keyword)
	print(name[0])
	r.extract_keywords_from_text(release[0])
	keyword = r.get_ranked_phrases()
	word.append(keyword)
	print(keyword)
	print(release[0])
	print(artist[0])
	print(word)
	

Findwords()
