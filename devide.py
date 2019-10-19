import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# client_credentials_manager = SpotifyClientCredentials(client_id='3e909e4b4f194e66b3865f64d9b99b77', client_secret='8d8d2d9416e845a9bef9d46b9e21b583')
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# results = sp.search(q='weezer', limit=20)
# for i, t in enumerate(results['tracks']['items']):
    # print(' ', i, t['name'])
	
#devide the dataset
data = pd.read_csv('train_triplets.csv', header = None)#'user_id','song_id','listen time'
data.columns = ['user_id','song_id','listen time']
user = data.user_id
#print(data.head())
user1 = data.user_id[0]#get the first user

print(user1)
data1 = data[data.user_id.isin([user1])]
#print(data1)
list1 = data1.values.tolist()
#print(list)

#cut the data base into a smaller one
my_df = pd.DataFrame(list1)
my_df.to_csv("smallexample/user1.csv", index = False, header = False)

user2 = data.user_id[1]#get the second user
data2 = data[data.user_id.isin([user2])]
list2 = data2.values.tolist()
my_df = pd.DataFrame(list2)
my_df.to_csv("smallexample/user2.csv", index = False, header = False)

# csvFile = open("smallexample/data1.csv", "w")
# writer = csv.writer(csvFile)
# i = 0
# while i < 100:
	# writer.writerows(list[i])
	# i = i + 1
# csvFile.close()