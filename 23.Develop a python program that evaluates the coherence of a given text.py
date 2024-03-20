import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_sentence_embeddings(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentence_embeddings = []
    for sentence in doc.sents:
        # Ignore empty sentences
        if len(sentence) > 1:
            sentence_embeddings.append(sentence.vector)
    return np.array(sentence_embeddings)

def compute_coherence_score(text):
    sentence_embeddings = compute_sentence_embeddings(text)
    num_sentences = len(sentence_embeddings)
    if num_sentences < 2:
        return 0  # Coherence score undefined for less than 2 sentences
    similarity_sum = 0
    num_pairs = 0
    for i in range(num_sentences):
        for j in range(i+1, num_sentences):
            similarity = cosine_similarity([sentence_embeddings[i]], [sentence_embeddings[j]])[0][0]
            similarity_sum += similarity
            num_pairs += 1
    coherence_score = similarity_sum / num_pairs
    return coherence_score

if __name__ == "__main__":
    # Example text
    text = """
    The quick brown fox jumps over the lazy dog.
    This is a test sentence for evaluating coherence.
    Coherence is important for understanding text.
    """

    # Compute coherence score
    coherence_score = compute_coherence_score(text)
    print("Coherence Score:", coherence_score)
