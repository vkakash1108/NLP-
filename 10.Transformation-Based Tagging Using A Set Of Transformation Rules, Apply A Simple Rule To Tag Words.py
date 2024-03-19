import nltk
def apply_rule(word, tag, rules):
    for rule in rules:
        if word in rule[0]:
            if tag in rule[1]:
                return rule[1]
    return tag
rules = [
    (r'\d+', 'CD'),               
    (r'[a-zA-Z]+(ed|ing|es|)?$', 'VB'),  
    (r'[a-zA-Z]+(ly|ment)?$', 'RB'),       
    (r'[a-zA-Z]+(able|ible)?$', 'JJ'),     
    (r'\b(a|an|the)\b', 'DT'),            
    (r'[a-zA-Z]+', 'NN')                  
]
text = "The quick brown fox jumps over the lazy dog"
words = nltk.word_tokenize(text)

tagged_words = []
for word in words:
    tag = apply_rule(word, 'NN', rules)
    tagged_words.append((word, tag))

print(tagged_words)
