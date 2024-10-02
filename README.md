# UIChatbot_throughCallAPI

### 1. HOW TO RUN
Khi build UI, bạn ấn: pip install streamlit => Auto được đề xuất tạo .env (cùng với auto cài requirements.txt)
```bash
.venv\Scripts\activate
```
### PROMPTING AND TUNING PROMPTING: 

- Update từ QA Assistant lên chatbot với khả năng ghi nhớ hội thoại
Từ API hỏi gì đáp nấy của con bot RAG . Muốn build code thành con chatbot có khả năng ghi nhớ hội thoại thì sao nhỉ?

QA Assistant: 
```
        "prompt": [
            {
                "role": "system",
                "content": "You are an intelligent assistant. Please answer the question based on content of knowledge base. When all knowledge base content is irrelevant to the question, your answer must include the sentence 'The answer you are looking for is not found in the knowledge base!'. Answers need to consider chat history. Knowledge base content is as following:\n{{REFERENCE}}"
            },
            {
                "role": "user",
                "content": "The question is: '{{TEXT}}'.\nAnswer only the question and do not output any other words."
            }
        ],

```

Chatbot thân thiện: (Sự khác biệt giữa bạn bot trả lời thẳng thắn "Answer only the question and do not output any other words với bạn bot thân thiện")
```
        "prompt": [
            {
                "role": "system",
                "content": "You are a friendly and helpful assistant for CSKH-StepUpEducation. Your responses should be natural, engaging, and conversational. Use the knowledge base content to inform your answers, but present the information in a smooth, chatbot-like manner. If the knowledge base doesn't contain relevant information, politely inform the user. Here's the knowledge base content:\n{{REFERENCE}}"
            },
        ] + [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages[-5:]] + [
            {
                "role": "user",
                "content": f"The user asks: '{prompt}'. Please provide a friendly, conversational response that addresses their question while considering the chat history above."
            }
        ],

```