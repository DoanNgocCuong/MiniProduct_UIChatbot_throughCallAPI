import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_APIquery_historychat(api_url, api_key, user_input_prompt, chat_history):
    headers = {'Content-Type': 'application/json'}
    data = {
        "api_key": api_key,
        "text": user_input_prompt,
        "top_k": 5,
        "return_doc": False,
        "prompt": [
            {
                "role": "system",
                "content": (
                    "You are a friendly and helpful assistant for CSKH-StepUpEducation. "
                    "Your responses should be natural, engaging, and conversational. "
                    "Use the knowledge base content to inform your answers, but present "
                    "the information in a smooth, chatbot-like manner. If the knowledge base "
                    "doesn't contain relevant information, politely inform the user. "
                    "Here's the knowledge base content:\n{{REFERENCE}}"
                ),
            },
        ] + chat_history[-5:] + [
            {
                "role": "user",
                "content": (
                    f"The user asks: '{user_input_prompt}'. Please provide a friendly, conversational "
                    "response that addresses their question while considering the chat history above."
                ),
            }
        ],
        "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
    }
    
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        if result is None:
            return "Error: Received empty response from API", chat_history
        content = result.get('result', {}).get('pred_answer_list', '')
        # Update chat history
        chat_history.append({"role": "user", "content": user_input_prompt})
        chat_history.append({"role": "assistant", "content": content})
        return content, chat_history
    else:
        return f"Error: {response.status_code} - {response.text}", chat_history

# Example usage
if __name__ == "__main__":
    API_URL = os.getenv('API_URL')
    API_KEY = os.getenv('API_KEY')
    chat_history = []
    
    if not API_URL or not API_KEY:
        print("Error: API_URL or API_KEY not found in environment variables")
    else:
        while True:
            prompt = input("Enter your question (or type 'exit' to quit): ")
            if prompt.lower() in ['exit', 'quit']:
                break
            result, chat_history = test_APIquery_historychat(API_URL, API_KEY, prompt, chat_history)
            print(result)
