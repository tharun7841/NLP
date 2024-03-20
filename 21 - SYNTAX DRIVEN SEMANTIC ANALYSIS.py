import nltk
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

# Download necessary resources (uncomment if not already downloaded)
# nltk.download('punkt')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

def extract_noun_phrases(sentence):
    # Tokenize the sentence
    words = nltk.word_tokenize(sentence)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)

    # Use named entity chunking to identify noun phrases
    chunked_sentence = ne_chunk(pos_tags)

    # Extract noun phrases and their meanings
    noun_phrases = []
    for subtree in chunked_sentence:
        if isinstance(subtree, Tree) and subtree.label() == 'NP':
            # Extract noun phrases
            noun_phrase = " ".join(word for word, _ in subtree.leaves())
            # Extract meanings by joining words and tags
            meanings = " ".join(f"{word}/{tag}" for word, tag in subtree.leaves())
            noun_phrases.append((noun_phrase, meanings))

    return noun_phrases

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
noun_phrases = extract_noun_phrases(sentence)

# Print the results
print("Original Sentence:", sentence)
print("Extracted Noun Phrases and Meanings:")
for noun_phrase, meanings in noun_phrases:
    print(f"Noun Phrase: {noun_phrase} | Meanings: {meanings}")
