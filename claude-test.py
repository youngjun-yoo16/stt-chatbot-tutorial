import anthropic
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv() 

# Replace with your API key from Anthropic
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize the client
client = anthropic.Client(api_key=API_KEY)

print("Welcome to the Claude CLI Chatbot!")

while True:
    # Get user input
    user_input = input("You: ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break

    try:
        # Get a response from Claude
        response = client.completions.create(
            prompt=f"Human: {user_input}\n\nAssistant:",
            stop_sequences=["\nHuman"],
            max_tokens_to_sample=1000,
            model="claude-v1"  # Specify the model if required
        )

        # Print Claude's response
        print(f"Claude: {response['completion']}")

    except Exception as e:
        print(f"Error: {e}")

print("Goodbye!")
