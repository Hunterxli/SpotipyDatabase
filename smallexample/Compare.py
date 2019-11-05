import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from itertools import product

num = 1
#songnum = 1
keyword = []
test = ["going", "done", "teaching", "better", "thicker", "die", "beautifully", "nothing"]
tagged_sent = []
lenth = 0

def get_wordnet_pos(tag):
	if tag.startswith('J'):
		return wn.ADJ
	elif tag.startswith('V'):
		return wn.VERB
	elif tag.startswith('N'):
		return wn.NOUN
	elif tag.startswith('R'):
		return wn.ADV
	else:
		return None

def Compare(songnum):
	data = pd.read_csv('keywords/the{}user-{}-song.csv'.format(num, songnum))
	keyword = data.keywords[0]
	keyword = keyword.split(',')
	#keyword = test # test
	print(keyword)
	# get the original word
	tagged_sent = nltk.pos_tag(keyword)
	print(tagged_sent)
	# wnl = ()
	# lemmas_sent = []
	# for tag in tagged_sent:
		# wordnet_pos = get_wordnet_pos(tag[1]) or wn.NOUN
		# lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))
		# #print(tag)
	# print(lemmas_sent)
	return tagged_sent
	# #return songnum
	
	# # get the synonyms
	# i = 0
	# while(i < len(keyword)):
		
		# result = wn.morphy(keyword[i], wn.NOUN)
		# if result != None:
			# print("{}:".format(keyword[i]))
			# print("synonyms:")
			# synonyms = []
			# for syn in wn.synsets(keyword[i]):
				# for l in syn.lemmas():
					# synonyms.append(l.name())
			# print(set(synonyms))
			# print("\n")
		# else:
			# print("couldn't find any synonym")
			# print("\n")
		# i = i + 1


def Calculate(firstsong, secondsong):
	song1 = []
	song2 = []
	song1 = Compare(firstsong)
	song2 = Compare(secondsong)
	i = 0
	while(i < len(song2)):
		k = 0
		while(k < len(song1)):
			sense1 = wn.synsets(song1[k])[0]
			sense2 = wn.synsets(song2[i])[0]
			print(song1[k]+" and "+song2[i]+":")
			print(sense1.wup_similarity(sense2))
			k = k + 1
		#print(song2[i])
		i = i + 1
			
			
	
data2 = pd.read_csv('user{}_songname.csv'.format(num))
lenth = len(data2) + 1
print(lenth)
s1 = 1
s2 = 3
Calculate(s1, s2)
# s1 = 1
# while(s1 < lenth):
	# s2 = 2
	# while(s2 < lenth):
		# Calculate(s1, s2)
		# s2 = s2 + 1
	# s1 = s1 + 1
	


	