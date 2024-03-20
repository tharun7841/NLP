import nltk
from nltk import PCFG
from nltk import parse

# Define a Probabilistic Context-Free Grammar (PCFG)
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | NP PP [0.25] | 'John' [0.25]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'man' [0.5] | 'dog' [0.5]
    V -> 'saw' [0.4] | 'chased' [0.6]
    P -> 'with' [0.3] | 'in' [0.7]
""")

# Create a probabilistic parser using the PCFG
parser = parse.EarleyChartParser(pcfg_grammar)

# Function to perform PCFG parsing for a sentence
def pcfg_parse(sentence):
    words = sentence.split()
    
    # Generate and print the most probable parse tree
    parses = parser.parse(words)
    most_probable_parse = max(parses, key=lambda tree: tree.prob())
    most_probable_parse.pretty_print()

# Example sentence
example_sentence = "the man saw a dog with a telescope"

# Perform PCFG parsing
pcfg_parse(example_sentence)
