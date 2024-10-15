# main.py

from APIBasicRAG_chatbot.backend_package.test_ChatAssistant_mongoDB_eachChat import ChatAssistantBackend
from frontend_package.frontend_v1 import ChatAssistantFrontend
import streamlit as st

import os
from dotenv import load_dotenv  # Add this import
load_dotenv()  # Load environment variables from .env file


# Configuration
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
MONGO_URI = os.getenv('MONGO_URI')  # Thay bằng chuỗi kết nối của bạn

def main():
    # Initialize backend and frontend
    backend = ChatAssistantBackend(API_URL, API_KEY, MONGO_URI)
    frontend = ChatAssistantFrontend()

    # Manage conversation ID
    if 'conversation_id' not in st.session_state:
        st.session_state['conversation_id'] = backend.create_conversation()

    conversation_id = st.session_state['conversation_id']

    # Display existing chat history
    frontend.display_chat_history()

    # Get user input
    prompt = frontend.get_user_input()

    if prompt:
        # Display user message
        frontend.display_user_message(prompt)
        # Update chat history with user message
        frontend.update_chat_history("user", prompt)
        # Log the user's message
        backend.log_message(conversation_id, {"role": "user", "content": prompt})

        # Prepare data for API request
        chat_history = frontend.get_chat_history()
        data = backend.prepare_data(prompt, chat_history)

        # Send API request
        response = backend.send_request(data)

        # Get response content
        content = backend.get_response_content(response)

        # Display assistant response
        if response.status_code == 200:
            frontend.display_assistant_message(content)
            # Update chat history with assistant message
            frontend.update_chat_history("assistant", content)
            # Log the assistant's message
            backend.log_message(conversation_id, {"role": "assistant", "content": content})
        else:
            frontend.display_error_message(content)

    # Option to start a new conversation
    if st.button('Start New Conversation'):
        st.session_state['conversation_id'] = backend.create_conversation()
        frontend.clear_chat_history()

if __name__ == "__main__":
    main()
