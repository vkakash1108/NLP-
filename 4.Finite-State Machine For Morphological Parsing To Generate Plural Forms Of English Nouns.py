import re

def pluralize(word):
    rules = [
        ['[sxz]$', '$', 'es'],
        ['[^aeioudgkprt]h$', '$', 'es'],
        ['(qu|[^aeiou])y$', 'y$', 'ies'],
        ['$', '$', 's']
    ]

    for rule in rules:
        pattern, search, replace = rule
        if re.search(pattern, word):
            return re.sub(search, replace, word)

print(pluralize("cat"))  
print(pluralize("dog"))  
print(pluralize("knife"))  
print(pluralize("potato"))  

