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
	k = 0
	while(k < i):
		word = []
		r = Rake()
		r.extract_keywords_from_text(name[k])
		keyword = r.get_ranked_phrases()
		keyword = ",".join(keyword)
		word.append(keyword)
		#print(keyword)
		#print(name[0])
		r.extract_keywords_from_text(release[k])
		keyword = r.get_ranked_phrases()
		keyword = ",".join(keyword)
		word.append(keyword)
		#print(keyword)
		print(name[k])
		print(release[k])
		print(artist[k])
		print(word)
		words = ",".join(word)
		fileHeader = ["song_name", "song_artist", "keywords", 'listen_time']
		csvFile = open("keywords/the{}user-{}-song.csv".format(num, k + 1), "w", newline='', encoding='utf-8')
		writer = csv.writer(csvFile)
		writer.writerow(fileHeader)
		d = [name[k], artist[k], words, listen[k]]
		writer.writerow(d)
		csvFile.close()
		k = k + 1
	
while(num < 101):
	Findwords()
	num = num + 1
	
