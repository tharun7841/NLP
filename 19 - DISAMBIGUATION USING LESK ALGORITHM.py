from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk

def word_sense_disambiguation(context_sentence, target_word):
    # Tokenize the context sentence
    context_tokens = word_tokenize(context_sentence)

    # Use the Lesk algorithm for WSD
    sense = lesk(context_tokens, target_word)

    if sense:
        # Display the result
        print(f"Target Word: {target_word}")
        print(f"Context Sentence: {context_sentence}")
        print(f"Word Sense: {sense.name()}")
        print(f"Definition: {sense.definition()}")
        print("\n")
    else:
        print(f"No suitable sense found for the target word '{target_word}'.\n")

# Example usage
context_sentence = "I went to the bank to deposit some money."
target_word1 = "bank"
word_sense_disambiguation(context_sentence, target_word1)

context_sentence = "The river bank was full of flowers."
target_word2 = "bank"
word_sense_disambiguation(context_sentence, target_word2)
