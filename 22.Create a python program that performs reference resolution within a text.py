import spacy


nlp = spacy.load("en_core_web_sm")

def resolve_references(text):
    
    doc = nlp(text)

    
    references = {}

    
    for token in doc:
        if token.dep_ in ["pronoun"]:
            
            resolved_reference = find_antecedent(token)

            
            references[token.text] = resolved_reference

    
    resolved_text = " ".join(references.get(token.text, token.text) for token in doc)

    return resolved_text

def find_antecedent(pronoun_token):
    
    for ancestor in pronoun_token.ancestors:
        if ancestor.dep_ in ["nsubj", "attr"]:
            return ancestor.text


    for sentence in pronoun_token.doc.sents:
        for token in sentence:
            if token.dep_ in ["nsubj", "attr"]:
                return token.text

    
    return ""

if __name__ == "__main__":
    
    example_text = "John has a cat. He loves it. The cat is very playful."

    
    resolved_text = resolve_references(example_text)

    
    print("Original Text:")
    print(example_text)
    print("\nResolved Text:")
    print(resolved_text)
