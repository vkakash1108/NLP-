import random
def generate_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    model = {}
    for word1, word2 in bigrams:
        if word1 in model:
            model[word1].append(word2)
        else:
            model[word1] = [word2]
    return model
def generate_text_bigram(model, num_words=50):
    current_word = random.choice(list(model.keys()))
    text = current_word
    for _ in range(num_words - 1):
        if current_word in model:
            next_word = random.choice(model[current_word])
            text += " " + next_word
            current_word = next_word
        else:
            break
    return text
text = input("Enter your text: ")
model = generate_bigram_model(text)
generated_text = generate_text_bigram(model)
print("Generated text:")
print(generated_text)
