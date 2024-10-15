import requests
import json
import os
import sys
# Add the parent directory to sys.path để import được config.py
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import config  # Now we can import config from the parent directory
from dotenv import load_dotenv

# method: POST
# endpoint: https://open.larksuite.com/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records

# Link base: https://csg2ej4iz2hz.sg.larksuite.com/base/HTJ6bPPPfaelL5sKDVglGHHOgCg?table=tblpgKokUDFf7cFn
# Parameters
app_token = config.APP_BASE_TOKEN
table_id = config.BASE_TABLE_ID
print(app_token)
print(table_id)

# Load environment variables from .env file
load_dotenv()
bearer_token = os.getenv('LARK_BEARER_TOKEN')
print(bearer_token)

url = f"https://open.larksuite.com/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"

# Body: 
## Các cột cần có sẵn trong Base:
payload = json.dumps({
    "fields": {
        "Multi-select column": [
            "Option1",
            "Option2"
        ],
        "Single option column": "Option1",
        "Text column": "Example Text"
    }
})

# Authorization và Header
# Authorization: Giá trị của access token (dạng "Bearer access_token")
# Content-Type: "application/json; charset=utf-8"
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

try:
    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")