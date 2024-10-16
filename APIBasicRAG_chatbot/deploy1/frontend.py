import streamlit as st

def initialize_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_user_input():
    return st.chat_input("What is your question?")

def display_user_message(prompt):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

def display_assistant_message(content):
    with st.chat_message("assistant"):
        st.markdown(content)
    st.session_state.messages.append({"role": "assistant", "content": content})

def display_error(status_code, text):
    with st.chat_message("assistant"):
        st.error(f"Error: {status_code} - {text}")