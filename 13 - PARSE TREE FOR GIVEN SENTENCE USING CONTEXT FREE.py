import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define a simple context-free grammar
cfg = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | 'I'
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'caught'
""")

# Create a parser with the defined CFG
parser = ChartParser(cfg)

# Function to generate a parse tree for a sentence
def generate_parse_tree(sentence):
    words = sentence.split()
    parses = parser.parse(words)
    
    for tree in parses:
        tree.pretty_print()

# Example sentence
example_sentence = "I caught the cat"

# Generate and print the parse tree
generate_parse_tree(example_sentence)
