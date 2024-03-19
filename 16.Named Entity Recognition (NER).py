import spacy

def perform_ner(text):
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")

text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California."

perform_ner(text)
