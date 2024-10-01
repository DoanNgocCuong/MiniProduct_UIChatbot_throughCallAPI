import requests
import json
import streamlit as st

url = 'https://mentor-dev.fpt.ai/math-centerpiece-model'
headers = {'Content-Type': 'application/json'}

st.title("Math Calculation Assistant")

user_question = st.text_input("Enter your math question:", "Calculate 100 + 400 - 250. Just output the answer.")

if st.button("Calculate"):
    data = {
        "messages": [
            {
                "role": "system",
                "content": "Please reason step by step, and put your final answer within \\boxed{}."
            },
            {
                "role": "user",
                "content": user_question
            }
        ]
    }

    print("Sending request with data:", json.dumps(data, indent=2))  # Print request data

    response = requests.post(url, headers=headers, json=data)

    print("Response status code:", response.status_code)  # Print response status code

    if response.status_code == 200:
        result = response.json()
        print("Raw response:", json.dumps(result, indent=2))  # Print raw response
        content = result.get('response', {}).get('response', '')
        formatted_result = content.replace("\\n", "\n").replace("\\(", "$").replace("\\)", "$").replace("\\[", "$$").replace("\\]", "$$")
        print("Formatted result:", formatted_result)  # Print formatted result
        st.markdown(f"Response:\n{formatted_result}")
    else:
        print("Error response:", response.text)  # Print error response
        st.error(f"Error: {response.status_code} - {response.text}")