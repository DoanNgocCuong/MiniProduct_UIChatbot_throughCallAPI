import streamlit as st
from deploy1_backend import send_request
from deploy1_frontend import (
    initialize_chat,
    display_chat_history,
    get_user_input,
    display_user_message,
    display_assistant_message,
    display_error
)

def main():
    st.title("CSKH-StepUpEducation Assistant")

    initialize_chat()
    display_chat_history()

    if prompt := get_user_input():
        display_user_message(prompt)

        chat_history = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages[-5:]]
        content = send_request(prompt, chat_history)

        if content:
            display_assistant_message(content)
        else:
            display_error("Unknown", "Failed to get response from the server")

if __name__ == "__main__":
    main()