from nltk.corpus import wordnet

list1 = ['Compare', 'require']
list2 = ['choose', 'two copies', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
list = []

for word1 in list1:
	for word2 in list2:
		wordFromList1 = wordnet.synsets(word1)
		wordFromList2 = wordnet.synsets(word2)
		if wordFromList1 and wordFromList2: #Thanks to @alexis' note
			s = wordFromList1[0].wup_similarity(wordFromList2[0])
			list.append(s)
			print(word1 + " and " +word2 + ":")
			print(s)

#print(list)

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example_sent = "This is a sample sentence, showing off the stop words filtration."
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 