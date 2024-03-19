from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def lesk(word, sentence):
    sentence_tokens = set(word_tokenize(sentence.lower()))
    best_sense = None
    max_overlap = 0
    
    for synset in wordnet.synsets(word):
        signature = set(word_tokenize(synset.definition().lower()))
        signature.update(word_tokenize(" ".join(synset.examples()).lower()))
        overlap = len(sentence_tokens.intersection(signature))
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset
    
    return best_sense

word = "bank"
sentence = "He sat on the bank of the river and watched the sunset."

sense = lesk(word, sentence)
if sense:
    print("Word:", word)
    print("Sentence:", sentence)
    print("Best Sense:", sense)
    print("Definition:", sense.definition())
else:
    print("No sense found for the word:", word)
