# UIChatbot_throughCallAPI

### RUN
Khi build UI, bạn ấn: pip install streamlit => Auto được đề xuất tạo .env (cùng với auto cài requirements.txt)
```bash
.venv\Scripts\activate
```
### Update từ QA Assistant lên chatbot với khả năng ghi nhớ hội thoại
Từ API hỏi gì đáp nấy của con bot RAG . Muốn build code thành con chatbot có khả năng ghi nhớ hội thoại thì sao nhỉ?
```bash
        "prompt": [
            {
                "role": "system",
                "content": "You are an intelligent assistant. Please answer the question based on content of knowledge base and the chat history. When all knowledge base content is irrelevant to the question, your answer must include the sentence 'The answer you are looking for is not found in the knowledge base!'. Knowledge base content is as following:\n{{REFERENCE}}"
            },
        ] + [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages[-5:]] + [
            {
                "role": "user",
                "content": f"The question is: '{prompt}'.\nAnswer the question considering the chat history above."
            }
        ],
```