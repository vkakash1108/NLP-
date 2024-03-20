import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def extract_noun_phrases(sentence):
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    
    grammar = r"""
        NP: {<DT>?<JJ>*<NN>}   # Chunk sequences of DT, JJ, and NN
            {<NNP>+}           # Chunk sequences of proper nouns
    """
    chunk_parser = nltk.RegexpParser(grammar)
    parsed_sentence = chunk_parser.parse(tagged_tokens)
    
    noun_phrases = []
    for subtree in parsed_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
        noun_phrases.append(' '.join(word for word, tag in subtree.leaves()))
    
    return noun_phrases

def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    noun_phrases = extract_noun_phrases(sentence)
    print("Noun phrases:", noun_phrases)

if __name__ == "__main__":
    main()
