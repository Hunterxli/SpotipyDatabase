import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import wordnet as wn

num = 1
songnum = 1
keyword = []
def Compare():
	data = pd.read_csv('keywords/the{}user-{}-song.csv'.format(num, songnum))
	data2 = pd.read_csv('user{}_songname.csv'.format(num))
	lenth = len(data2)
	keyword = data.keywords[0]
	keyword = keyword.split(',')
	print(keyword)
	
	i = 0
	while(i < len(keyword)):
		result = wn.morphy(keyword[i], wn.NOUN)
		if result != None:
			print("{}:".format(keyword[i]))
			print("synonyms:")
			synonyms = []
			for syn in wn.synsets(keyword[i]):
				for l in syn.lemmas():
					synonyms.append(l.name())
			print(set(synonyms))
			print("\n")
		else:
			print("not a noun")
			print("\n")
		i = i + 1

Compare()
	