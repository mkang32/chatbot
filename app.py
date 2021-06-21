import pickle
import numpy as np
import random
import json
from keras.models import load_model 
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# the below lines need to be run one time
# nltk.download('punkt')
# nltk.download('wordnet')


words = pickle.load(open('words.pkl', 'rb'))
model = load_model('chatbot_model.h5')
classes = pickle.load(open('classes.pkl', 'rb'))
intents = json.load(open('intents.json', 'rb'))

def clean_up_sentence(sentence):
	"""
	Tokenize and lemmatize 
	"""
	# tokenizing: split words into an array (e.g. "How are you?" --> ["How", "are", "you", "?"])
	sentence_words = nltk.word_tokenize(sentence)
	# lemmatizing: find short form for words (e.g. apples --> apple)
	sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
	return sentence_words

def get_bag_of_words(sentence, words):
	"""
	Turn sentence into an array of 0 and 1 given words
	"""
	sentence_words = clean_up_sentence(sentence)

	bag = [0] * len(words)
	for s in sentence_words:
		for i, w in enumerate(words):
			if s == w:
				bag[i] = 1
	return np.array(bag)

def predict_class(sentence, words, model):
	p = get_bag_of_words(sentence, words)
	res = model.predict(np.array([p]))  # [[p0, p1, ...]]
	results = [[i, p] for i, p in enumerate(res[0])]
	results.sort(key=lambda x: x[1], reverse=True) # [[i, p(i)], ...]
	most_probable = results[0]
	
	# TODO: handle when the probability less than threshold

	return [classes[most_probable[0]], most_probable[1]]  # [class name, probability]

def get_response(class_name, intents):
	for intent in intents.get('intents'): 
		if intent.get('tag') == class_name:
			res = random.choice(intent.get('responses'))
			break
	return res

def chatbot_response(msg, words=words, model=model, intents=intents):
	class_name, prob = predict_class(msg, words, model)
	res = get_response(class_name, intents)
	return res 


import sys

print()
print("*"*10 + "Start of Conversation" + "*"*10)
print("Say 'exit' to stop the conversation.....")
sentence = input("Bot: How can I help you? \nYou:")
while sentence != 'exit':
	res = chatbot_response(sentence)
	sentence = input(f"Bot: {res} \nYou:")
print("*"*10 + "End of Conversation" + "*"*10)

