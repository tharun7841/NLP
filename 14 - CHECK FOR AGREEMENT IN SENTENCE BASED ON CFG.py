import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define a context-free grammar for subject-verb agreement
cfg = CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> 'he' | 'she' | 'it'
    NP_PL -> 'they' | 'we' | 'cats' | 'dogs'
    VP_SG -> V_SG | V_SG NP_SG
    VP_PL -> V_PL | V_PL NP_PL
    V_SG -> 'runs' | 'jumps' | 'sleeps'
    V_PL -> 'run' | 'jump' | 'sleep'
""")

# Create a parser with the defined CFG
parser = ChartParser(cfg)

# Function to check subject-verb agreement in a sentence
def check_agreement(sentence):
    words = sentence.split()
    parses = parser.parse(words)
    
    for tree in parses:
        print("Parse Tree:")
        tree.pretty_print()

        # Check for subject-verb agreement
        if 'VP_SG' in str(tree) and 'NP_PL' in str(tree):
            print("Subject-verb disagreement: Singular subject with plural verb.")
            return False
        elif 'VP_PL' in str(tree) and 'NP_SG' in str(tree):
            print("Subject-verb disagreement: Plural subject with singular verb.")
            return False

        print("Subject-verb agreement: Correct.")
        return True

# Example sentence
example_sentence = "they run"

# Check subject-verb agreement
check_agreement(example_sentence)
