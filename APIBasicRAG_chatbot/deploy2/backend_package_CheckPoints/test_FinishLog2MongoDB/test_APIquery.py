import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_APIquery(api_url, api_key, user_input_prompt):
    """
    Test query RAG API

    Args:
        api_url (str): API URL
        api_key (str): API key
        user_input_prompt (str): User input prompt

    Returns:
        str: Assistant response
    """
    headers = {'Content-Type': 'application/json'}
    data = {
        "api_key": api_key,
        "text": user_input_prompt,
        "top_k": 5,
        "return_doc": False,
        "prompt": [
            {
                "role": "system",
                "content": "You are a AI Assistant."
            },
            {
                "role": "user",
                "content": user_input_prompt
            }
        ],
        "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
    }
    
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        if result is None:
            return "Error: Received empty response from API"
        content = result.get('result', {}).get('pred_answer_list', '')
        return content
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
if __name__ == "__main__":
    API_URL = os.getenv('API_URL')
    API_KEY = os.getenv('API_KEY')
    
    prompt = input("Enter your question: ")
    
    if not API_URL or not API_KEY:
        print("Error: API_URL or API_KEY not found in environment variables")
    else:
        result = test_APIquery(API_URL, API_KEY, prompt)
        print(result)
