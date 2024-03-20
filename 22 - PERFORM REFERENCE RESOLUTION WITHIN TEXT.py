import spacy
import neuralcoref

# Load spaCy and neuralcoref
nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

def resolve_references(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Print resolved references
    for cluster in doc._.coref_clusters:
        main_reference = cluster.main
        references = [mention.text for mention in cluster.mentions]
        print(f"Main reference: {main_reference}, References: {references}")

# Example usage
text = "John and Mary went to the park. They enjoyed their time there. Later, John and Mary had lunch."
resolve_references(text)
