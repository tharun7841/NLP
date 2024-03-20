from transformers import pipeline

def recognize_dialog_acts(conversation):
    # Load the pre-trained model for dialog act recognition
    dialog_act_recognizer = pipeline("utterance-type")

    # Perform dialog act recognition on the entire conversation
    results = dialog_act_recognizer(conversation)

    return results

# Example usage
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."},
    {"role": "assistant", "content": "Why don't scientists trust atoms?"}
]

dialog_acts = recognize_dialog_acts(conversation)

# Print the recognized dialog acts
print("Recognized Dialog Acts:")
for utterance, result in zip(conversation, dialog_acts):
    print(f"{utterance['role']} ({utterance['content']}): {result['utterance_type']}")
