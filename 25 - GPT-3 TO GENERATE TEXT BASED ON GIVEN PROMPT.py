import openai

# Set your OpenAI GPT-3 API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def generate_text(prompt):
    # Call the OpenAI GPT-3 API to generate text based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3 engine
        prompt=prompt,
        max_tokens=150,  # Adjust max_tokens as needed
        temperature=0.7  # Adjust temperature for creativity
    )

    # Extract and return the generated text from the API response
    generated_text = response.choices[0].text.strip()
    return generated_text

# Example usage
prompt = "Once upon a time in a land far, far away,"
generated_text = generate_text(prompt)

# Print the generated text
print("Generated Text:")
print(generated_text)
