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
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.tokenize import RegexpTokenizer

num1 = 1 #user 1
num2 = 2 #user 2
#songnum = 1
keyword = []
songname = ""
test = ["going", "done", "teaching", "better", "thicker", "die", "beautifully", "nothing"]
tagged_sent = []
lenth = 0
word1 = ""
word2 = ""
s = 0 
wordcomp1 = []
wordcomp2 = []
compreslut = []
arry_s1 = []
arry_s2 = []

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

def Compare(num, songnum):
	data = pd.read_csv('keyword/the{}user-{}-song.csv'.format(num, songnum))
	keyword1 = data.keywords[0]
	songname = data.song_name[0]
	keyword = keyword1.split(',')
	#keyword = test # test
	print(keyword)
	# get the original word
	#tagged_sent = nltk.pos_tag(keyword)
	#print(tagged_sent)
	# wnl = ()
	# lemmas_sent = []
	# for tag in tagged_sent:
		# wordnet_pos = get_wordnet_pos(tag[1]) or wn.NOUN
		# lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))
		# #print(tag)
	# print(lemmas_sent)
	stop_words = set(stopwords.words('english'))
	tokenizer = RegexpTokenizer(r'\w+')
	word_tokens = tokenizer.tokenize(keyword1)
	word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
	print("remove numbers：",word_tokens)
	word_tokens = " ".join(word_tokens)
	#print(word_tokens)
	
	# word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
	# print("remove numbers:", word_tokens)
	
	word_tokens = word_tokenize(word_tokens)
	filtered_sentence = [w for w in word_tokens if not w in stop_words] 
	filtered_sentence = [] 
	for w in word_tokens: 
		if w not in stop_words: 
			filtered_sentence.append(w) 
	#filtered_sentence = ",".join(filtered_sentence)
	print("remove stopwords:", filtered_sentence)
	
	return songname, filtered_sentence
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


def Calculate(num1, num2, firstsong, secondsong):
	song1 = []
	song2 = []
	songname1, x1 = Compare(num1, firstsong)
	songname2, x2 = Compare(num2, secondsong)
	song1 = x1
	song2 = x2
	print(song1)
	# print(num1)
	print(song2)
	# print(num2)
		
	i = 0
	for word1 in song1:
		for word2 in song2:
			#print(word1)
			#print(word2)
			wordFromList1 = wn.synsets(word1)
			wordFromList2 = wn.synsets(word2)
			if wordFromList1 and wordFromList2: 
				s = wordFromList1[0].wup_similarity(wordFromList2[0])
				if(s == None):
					s = 0
				mylist = list()
				mylist.append(s)
				print(word1 + " and " +word2 + ":")
				print(s)
				wordcomp1.append(word1)
				wordcomp2.append(word2)
				compreslut.append(s)
				arry_s1.append(songname1)
				arry_s2.append(songname2)
				
			
def Output(num1, num2):	
	data2 = pd.read_csv('user{}_songname.csv'.format(num1))
	data3 = pd.read_csv('user{}_songname.csv'.format(num2))
	lenth1 = len(data2) + 1
	lenth2 = len(data3) + 1
	print(lenth1)
	print(num1)
	print(lenth2)
	print(num2)
	# s1 = 1
	# s2 = 2
	# Calculate(s1, s2)
	
	s1 = 1
	while(s1 < lenth1):
	#while(s1 < 3):
		s2 = 1
		while(s2 < lenth2):
		#while(s2 < 3):

			print("the first song：", s1)
			print("the second song：", s2)
			Calculate(num1, num2, s1, s2)
			s2 = s2 + 1
		
		s1 = s1 + 1
	print(wordcomp1)
	print(wordcomp2)
	print(compreslut)
	i = 0

	csvFile = open("keyword2/the{}user-the{}user-calculation.csv".format(num1,num2), "w", newline='', encoding='utf-8')
	fileHeader = ["the first song", "the second song", "word1", 'word2', 'result']
	writer = csv.writer(csvFile)
	writer.writerow(fileHeader)
	while(i < len(compreslut)):
		print(wordcomp1[i]," and ", wordcomp2[i], ":", compreslut[i])
		d = [arry_s1[i], arry_s2[i], wordcomp1[i], wordcomp2[i], compreslut[i]]
		writer.writerow(d)
		i = i + 1

	csvFile.close()
	
	
#Output()
#num1 = 1 #user 1
#num2 = 2 #user 2
while(num1 < 6):
	num2 = 2
	while(num2 < 7):
		if(num1 < num2):
			Output(num1, num2)
			wordcomp1 = []
			wordcomp2 = []
			compreslut = []
			arry_s1 = []
			arry_s2 = []
		num2 = num2 + 1
	num1 = num1 + 1

	


	