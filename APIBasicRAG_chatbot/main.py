# main.py

import streamlit as st

from frontend_package.frontend_v1 import ChatAssistantFrontend
from backend_package.Threading_ExtendedChatAssistant_class_useCheckTenantAccessToken import ExtendedChatAssistant_Threading
from backend_package.createRecord_checkTenantAccessToken import create_record_with_checkTenantAccessToken
import os
import config


# Initialize the Streamlit interface
frontend = ChatAssistantFrontend()

# Load environment variables for backend configurations
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
LARK_APP_TOKEN = config.APP_BASE_TOKEN
LARK_TABLE_ID = config.BASE_TABLE_ID

if not API_URL or not API_KEY:
    st.error("API_URL or API_KEY not found in environment variables")
elif not LARK_APP_TOKEN or not LARK_TABLE_ID:
    st.error("Lark configurations not found in environment variables")
else:
    # Initialize the extended chat assistant
    assistant = ExtendedChatAssistant_Threading(
        API_URL,
        API_KEY,
        LARK_APP_TOKEN,
        LARK_TABLE_ID,
    )

    # Start a new conversation on page refresh
    assistant.start_new_conversation()

    # Display chat history
    frontend.display_chat_history()

    # Get user input from the frontend
    user_input = frontend.get_user_input()

    if user_input:
        # Display the user's input on the frontend
        frontend.display_user_message(user_input)

        # Get the assistant's response from the backend
        assistant_response = assistant.chat(user_input)

        # Display the assistant's response on the frontend
        frontend.display_assistant_message(assistant_response)

        # Update the chat history
        frontend.update_chat_history("user", user_input)
        frontend.update_chat_history("assistant", assistant_response)
