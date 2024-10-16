import requests
import json

url = 'http://103.253.20.13:9225/flashrag/rag/custom/generate'
headers = {
    'Content-Type': 'application/json',
}

def send_request(prompt, chat_history):
    data = {
        "api_key": "KB-20240930155359526614ElULtm4UAWTWqIpO0VFwAHUN9ntITvHe",
        "text": prompt,
        "top_k": 5,
        "return_doc": False,
        "prompt": [
            {
                "role": "system",
                "content": "You are a friendly and helpful assistant for CSKH-StepUpEducation. Your responses should be natural, engaging, and conversational. Use the knowledge base content to inform your answers, but present the information in a smooth, chatbot-like manner. If the knowledge base doesn't contain relevant information, politely inform the user. Here's the knowledge base content:\n{{REFERENCE}}"
            },
        ] + chat_history + [
            {
                "role": "user",
                "content": f"The user asks: '{prompt}'. Please provide a friendly, conversational response that addresses their question while considering the chat history above."
            }
        ],
        "format_content": "Doc {{INDEX}}: {{TITLE}}\n {{CONTENT}}\n"
    }

    print("Sending request with data:", json.dumps(data, indent=2))

    response = requests.post(url, headers=headers, json=data)
    print("Response status code:", response.status_code)

    if response.status_code == 200:
        result = response.json()
        print("Raw response:", json.dumps(result, indent=2))
        content = result.get('result', {}).get('pred_answer_list', '')
        print("Formatted result:", content)
        return content
    else:
        print("Error response:", response.text)
        return None