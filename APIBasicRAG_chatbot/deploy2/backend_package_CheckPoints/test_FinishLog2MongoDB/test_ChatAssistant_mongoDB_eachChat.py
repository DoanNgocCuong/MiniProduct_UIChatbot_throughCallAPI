import requests
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import datetime
import sys
import os

# Add the parent directory to sys.path để import được config.py
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import config  # Now we can import config from the parent directory

load_dotenv()

class ChatAssistant:
    """
    A class to interact with the CSKH-StepUpEducation assistant API, managing chat history and responses.
    """

    def __init__(self, api_url, api_key, mongo_uri):
        """
        Initialize the ChatAssistant with API URL, API key, and MongoDB URI.

        Args:
            api_url (str): The API endpoint URL.
            api_key (str): Your API key for authentication.
            mongo_uri (str): The MongoDB URI for connection.
        """
        self.api_url = api_url
        self.api_key = api_key
        self.mongo_uri = mongo_uri
        self.mongo_client = MongoClient(mongo_uri)
        self.db = self.mongo_client[config.DB_NAME]
        self.collection = self.db[config.COLLECTION_NAME]
        self.chat_history = []

    def chat(self, user_input_prompt):
        """
        Send a user prompt to the assistant and receive a response, managing chat history.

        Args:
            user_input_prompt (str): The user's input question.

        Returns:
            str: The assistant's response.
        """
        data = self._create_api_request_data(user_input_prompt)
        response = self._send_api_request(data)
        content = self._extract_response_content(response)
        # Update chat history
        self.chat_history.append({"role": "user", "content": user_input_prompt})
        self.chat_history.append({"role": "assistant", "content": content})
        self._log_to_mongodb(user_input_prompt, content)
        return content

    def _create_api_request_data(self, prompt):
        """
        Create the data structure for the API request.

        Args:
            prompt (str): The user's input question.

        Returns:
            dict: Formatted data for the API request.
        """
        data = {
            "api_key": self.api_key,
            "text": prompt,
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
            ] + self.chat_history[-5:] + [
                {
                    "role": "user",
                    "content": (
                        f"The user asks: '{prompt}'. Please provide a friendly, conversational "
                        "response that addresses their question while considering the chat history above."
                    ),
                }
            ],
            "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
        }
        return data

    def _send_api_request(self, data):
        """
        Send the API request and return the response.

        Args:
            data (dict): The request payload.

        Returns:
            requests.Response: The API response object.
        """
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.api_url, headers=headers, json=data)
        return response

    def _extract_response_content(self, response):
        """
        Extract the assistant's response content from the API response.

        Args:
            response (requests.Response): The API response object.

        Returns:
            str: The assistant's response or an error message.
        """
        if response.status_code == 200:
            result = response.json()
            if result is None:
                return "Error: Received empty response from API"
            content = result.get('result', {}).get('pred_answer_list', '')
            return content
        else:
            error_message = f"Error: {response.status_code} - {response.text}"
            return error_message

    def _log_to_mongodb(self, user_input, assistant_response):
        """
        Log the chat interaction to MongoDB.

        Args:
            user_input (str): The user's input question.
            assistant_response (str): The assistant's response.
        """
        log_entry = {
            "timestamp": datetime.datetime.utcnow(),
            "user_input": user_input,
            "assistant_response": assistant_response
        }
        self.collection.insert_one(log_entry)
        print("Log entry inserted successfully")

# Example usage
if __name__ == "__main__":
    # get API_URL, API_KEY, MONGO_URI from environment variables
    API_URL = os.getenv('API_URL')
    API_KEY = os.getenv('API_KEY')
    MONGO_URI = os.getenv('MONGO_URI')

    if not API_URL or not API_KEY or not MONGO_URI:
        print("Error: API_URL, API_KEY, or MONGO_URI not found in environment variables")
    else:
        assistant = ChatAssistant(API_URL, API_KEY, MONGO_URI)
        while True:
            prompt = input("Enter your question (or type 'exit' to quit): ")
            if prompt.lower() in ['exit', 'quit']:
                break
            result = assistant.chat(prompt)
            print(result)
