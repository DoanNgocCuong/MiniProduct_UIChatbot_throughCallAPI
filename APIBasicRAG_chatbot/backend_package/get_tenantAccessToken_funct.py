import requests
import json

# Import config
# Add the parent directory to sys.path để import được config.py
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import config  # Now we can import config from the parent directory 


# Define app credentials
app_DoanNgocCuong_id = config.APP_DOANNGOCCUONG_ID
app_DoanNgocCuong_secret = config.APP_DOANNGOCCUONG_SECRET

def get_tenant_access_token():
    url = "https://open.larksuite.com/open-apis/auth/v3/tenant_access_token/internal"
    payload = json.dumps({
        "app_id": app_DoanNgocCuong_id,
        "app_secret": app_DoanNgocCuong_secret
    })

    headers = {
        'Content-Type': 'application/json'
    }

    # Add this line to disable SSL certificate verification
    requests.packages.urllib3.disable_warnings()
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response.json().get('tenant_access_token')

# Example usage
if __name__ == "__main__":
    result = get_tenant_access_token()
    print(result)