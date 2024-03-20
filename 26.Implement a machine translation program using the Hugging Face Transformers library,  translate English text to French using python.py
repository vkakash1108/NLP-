from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, source_lang="en", target_lang="fr"):
    # Load pre-trained model and tokenizer
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Perform translation
    outputs = model.generate(**inputs)

    # Decode translated text
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

if __name__ == "__main__":
    # Example English text to translate
    english_text = "Hello, how are you?"

    # Translate English text to French
    french_text = translate_text(english_text, source_lang="en", target_lang="fr")
    print("Translated French Text:")
    print(french_text)
