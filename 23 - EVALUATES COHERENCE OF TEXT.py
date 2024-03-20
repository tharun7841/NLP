from sentence_transformers import SentenceTransformer, util

def evaluate_coherence(text):
    # Load a pre-trained BERT-based model for sentence embeddings
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Tokenize the text into sentences
    sentences = [s.strip() for s in text.split('.') if s.strip()]

    # Generate sentence embeddings
    sentence_embeddings = model.encode(sentences, convert_to_tensor=True)

    # Compute cosine similarity between consecutive sentence embeddings
    similarities = util.pytorch_cos_sim(sentence_embeddings[:-1], sentence_embeddings[1:]).tolist()

    # Calculate average similarity
    average_similarity = sum(similarities) / len(similarities)

    return average_similarity

# Example usage
text_to_evaluate = """
Natural Language Processing (NLP) is a subfield of artificial intelligence that deals with the interaction 
between computers and humans using natural language. It encompasses various tasks such as text 
processing, language understanding, and language generation. Coherence in a text is important to ensure 
that the information flows smoothly and is easy to understand.
"""

coherence_score = evaluate_coherence(text_to_evaluate)
print(f"Text Coherence Score: {coherence_score:.4f}")
