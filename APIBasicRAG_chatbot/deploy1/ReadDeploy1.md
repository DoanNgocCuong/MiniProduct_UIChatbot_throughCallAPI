- source `.venv/Scripts/activate`
- cd `deploy1`
Bởi vì trong deploy1_main.py đang set up
```
from deploy1_backend import send_request
from deploy1_frontend import (
    initialize_chat,
    display_chat_history,
    get_user_input,
    display_user_message,
    display_assistant_message,
    display_error
)
```
- `streamlit run main_deploy1.py`

