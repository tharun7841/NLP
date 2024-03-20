import nltk
from nltk.corpus import wordnet

# Download necessary resources (uncomment if not already downloaded)
# nltk.download('wordnet')

def explore_word_meanings(word):
    # Get the synsets for the given word
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for the word '{word}'.")
        return

    # Display information for each synset
    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print(f"Hypernyms: {synset.hypernyms()}")
        print(f"Hyponyms: {synset.hyponyms()}")
        print("\n")

# Example usage
word_to_explore = "python"
explore_word_meanings(word_to_explore)
