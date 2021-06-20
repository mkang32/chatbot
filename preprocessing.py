import pickle
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
# the below lines need to be run one time
# nltk.download('punkt')
# nltk.download('wordnet')

words = pickle.load(open('words.pkl', 'rb'))

def clean_up_sentence(sentence):
	# tokenizing: split words into an array
	sentence_words = nltk.word_tokenize(sentence)
	# lemmatizing: find short form for words (e.g. apples --> apple)
	sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
	return sentence_words

def bag_of_words(sentence, words):
	sentence_words = clean_up_sentence(sentence)

	bag = [0] * len(words)
	for s in sentence_words:
		for i, w in enumerate(words):
			if s == w:
				bag[i] = 1
				print(f"found in bag: {w}")
	return bag

sentence = "She doesn't want to eat apples."
bag = bag_of_words(sentence, words)
print(bag)