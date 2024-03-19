import nltk
from nltk import pos_tag, word_tokenize
def perform_pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    return tagged_words
text = "NLTK is a powerful library for natural language processing."
tagged_words = perform_pos_tagging(text)

print("Original Text:", text)
print("Part-of-Speech Tagging Result:", tagged_words)

