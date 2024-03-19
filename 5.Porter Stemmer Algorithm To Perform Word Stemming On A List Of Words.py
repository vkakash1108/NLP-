from nltk.stem import PorterStemmer
def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words
def main():
    words = input("Enter a list of words separated by spaces: ").split()
    stemmed_words = stem_words(words)
    print("Original words:", words)
    print("Stemmed words:", stemmed_words)
if __name__ == "__main__":
    main()
