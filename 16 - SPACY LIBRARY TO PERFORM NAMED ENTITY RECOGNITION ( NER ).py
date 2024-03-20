import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function to perform Named Entity Recognition
def perform_ner(text):
    # Process the text using SpaCy NLP pipeline
    doc = nlp(text)
    
    # Extract and print named entities
    print("Named Entities:")
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")

# Example text
example_text = "Apple Inc. is planning to open a new store in Paris next month."

# Perform Named Entity Recognition
perform_ner(example_text)
