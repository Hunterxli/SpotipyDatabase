import csv
import pandas as pd
import numpy as np
import os
import time
from rake_nltk import Rake
from google.cloud import translate_v2 as translate



num = 5
name = []
release = []
artist = []
listen = []
word = []
def Findwords(num):
	name = []
	release = []
	artist = []
	listen = []
	word = []
	data = pd.read_csv('user%s_songname.csv' %(num))
	data.columns = ['song_name','song_release','song_artist', 'listen_time']
	i = 0
	while(i < len(data)):
		print(i)
		song_name = data.song_name[i]
		song_release = data.song_release[i]
		song_artist = data.song_artist[i]
		listen_time = data.listen_time[i]
		
		#translate the language to English
		target = 'en'
		translate_client = translate.Client()
		song_name = translate_client.translate(song_name, target_language=target)
		name.append(song_name['translatedText'])
		print(song_name['translatedText'])
		song_release = translate_client.translate(song_release, target_language=target)
		release.append(song_release['translatedText'])
		print(song_release['translatedText'])
		song_artist = translate_client.translate(song_artist, target_language=target)
		artist.append(song_artist['translatedText'])
		print(song_artist['translatedText'])
		listen.append(listen_time)
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
		print(keyword)
		print(name[0])
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
		csvFile = open("keyword2/the{}user-{}-song.csv".format(num, k + 1), "w", newline='', encoding='utf-8')
		writer = csv.writer(csvFile)
		writer.writerow(fileHeader)
		d = [name[k], artist[k], words, listen[k]]
		writer.writerow(d)
		csvFile.close()
		k = k + 1
	
while(num < 7):
	Findwords(num)
	num = num + 1
	
