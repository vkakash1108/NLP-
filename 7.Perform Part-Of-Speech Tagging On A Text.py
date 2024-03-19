import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    return tagged_words
text = input("Enter your text: ")
tagged_text = pos_tagging(text)
print("Tagged text:")
print(tagged_text)
