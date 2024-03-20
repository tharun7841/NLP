from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, source_lang='en', target_lang='fr'):
    # Load pre-trained MarianMT model and tokenizer
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize and translate the input text
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

    return translated_text

# Example usage
english_text = "Hello, how are you? This is a simple translation example."

translated_text = translate_text(english_text, source_lang='en', target_lang='fr')

# Print the translated text
print("Original Text (English):", english_text)
print("Translated Text (French):", translated_text)
