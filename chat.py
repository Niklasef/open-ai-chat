import os
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("Enter your message: ")

    # Check if user wants to continue the conversation
    if user_input.lower() == 'quit':
        break

    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    # Extract the assistant's message
    assistant_message = response.choices[0].message

    # Append the assistant's message to the 'messages' list
    messages.append(assistant_message)

    print(f"Assistant says: {assistant_message['content']}")

