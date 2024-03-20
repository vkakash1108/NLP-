import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def recognize_dialog_act(utterance):
    # Tokenize the utterance
    tokens = word_tokenize(utterance.lower())

    # Remove stopwords
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]

    # Identify dialog act based on the first word
    if filtered_tokens:
        first_word = filtered_tokens[0]
        if first_word == 'what':
            return 'question'
        elif first_word in ['can', 'could', 'will', 'would', 'may', 'might', 'shall', 'should']:
            return 'request'
        elif first_word in ['i', 'we', 'you', 'he', 'she', 'they', 'it']:
            return 'statement'
    return 'other'

if __name__ == "__main__":
    # Example dialog
    dialog = [
        "What time is it?",
        "Can you pass the salt, please?",
        "I'm going to the store.",
        "Could you help me with this?"
    ]

    # Recognize dialog acts for each utterance
    for utterance in dialog:
        dialog_act = recognize_dialog_act(utterance)
        print(f"Utterance: '{utterance}' - Dialog Act: {dialog_act}")
