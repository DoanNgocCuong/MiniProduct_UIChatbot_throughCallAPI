Cấu trúc thư mục

```
APIBasicRAG_chatbot/
│
├── backend_package/
│   ├── ChatAssistant_class.py                      # Your ChatAssistant base class
│   ├── ExtendedChatAssistant_class.py              # Extended class with threading
│   ├── createRecord_checkTenantAccessToken.py      # Function to log records to Lark Base
│   ├── createRecord_tenantAccessToken.py           # Tenant Access Token related file
│   ├── get_tenantAccessToken_funct.py              # Functions to get tenant access token
│   ├── Threading_ExtendedChatAssistant_class_useCheckTenantAccessToken.py # Threaded extended assistant using tenant token
│   └── refresh_user_access_token.md                # Markdown file for refreshing access tokens
│
├── frontend_package/
│   ├── frontend.py                                 # Frontend interface file using Streamlit
│
├── main.py                                         # Main file to run the Streamlit app
├── .env                                            # Environment variables (API_KEY, API_URL, etc.)
└── config.py                                       # Configurations for Lark and other constants
```

Ensure you are running the Streamlit app from the correct directory. You should be in the `APIBasicRAG_chatbot` directory when you run the command:

```bash
streamlit run main.py
```

###
1. Create virtual env sử dụng `python -m venv .venv`
2. Truy vào vào `venv` bằng run Terminal: `.venv/Scripts/activate`
3. Install requirements.txt sử dụng `pip install -r requirements.txt`
4. Run test thử 1 số hàm độc lập xem còn hoạt động không, nhất là hàm backend chính `Threading_ExtendedChatAssistant`
5. `cd` vào `APIBasicRAG_chatbot`, sau đó `streamlit run main.py`
