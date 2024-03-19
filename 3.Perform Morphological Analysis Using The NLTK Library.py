import nltk
from nltk.corpus import wordnet
def morphological_analysis(word):
    synsets = wordnet.synsets(word)
    if synsets:
        for synset in synsets:
            print("Word:", synset.name())
            print("POS:", synset.pos())
            print("Definition:", synset.definition())
            print("Examples:", synset.examples())
            print()
    else:
        print("No morphological analysis found for the word:", word)
def main():
    word = input("Enter a word to perform morphological analysis: ")
    morphological_analysis(word)
if __name__ == "__main__":
    nltk.download('wordnet')
    main()
