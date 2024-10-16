# frontend.py

import streamlit as st

class ChatAssistantFrontend:
    def __init__(self):
        st.title("CSKH-StepUpEducation Assistant")
        self.initialize_session_state()

    def initialize_session_state(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_chat_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def get_user_input(self):
        return st.chat_input("What is your question?")

    def display_user_message(self, message):
        st.chat_message("user").markdown(message)

    def display_assistant_message(self, message):
        with st.chat_message("assistant"):
            st.markdown(message)

    def display_error_message(self, message):
        with st.chat_message("assistant"):
            st.error(message)

    def update_chat_history(self, role, content):
        st.session_state.messages.append({"role": role, "content": content})

    def get_chat_history(self):
        return st.session_state.messages

    def clear_chat_history(self):
        """
        Clear the chat history when starting a new conversation.
        """
        st.session_state.messages = []
