import requests
import json
import get_tenantAccessToken_funct

# Import config
# Add the parent directory to sys.path để import được config.py
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import config  # Now we can import config from the parent directory 
app_base_token = config.APP_BASE_TOKEN  # Your app_token
base_table_id = config.BASE_TABLE_ID  # Your table_id


fields_json = {
    "fields": {
        "Multi-select column": [
            "Option1",
            "Option2"
        ],
        "conversation_id": "Example Text"
    }
}

def create_record(app_base_token, base_table_id, tenant_access_token, fields_json):
    url = f"https://open.larksuite.com/open-apis/bitable/v1/apps/{app_base_token}/tables/{base_table_id}/records"
    payload = json.dumps(fields_json)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {tenant_access_token}'
    }

    # Add this line to disable SSL certificate verification
    requests.packages.urllib3.disable_warnings()
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    # Log response status and text for debugging
    print(f"Response status code: {response.status_code}")
    print(f"Response json: {response.json()}")
    return response

def create_record_with_checkTenantAccessToken(app_base_token, base_table_id, fields_json):

    # Get tenant_access_token from storage or generate a new one
    try:
        # Attempt to retrieve tenant_access_token from storage (e.g., file or database)
        # For this example, we'll assume it's stored in a file named 'tenantAccessToken_storage.txt'
        with open('tenantAccessToken_storage.txt', 'r') as file:
            tenant_access_token = file.read().strip()
            print("Tenant token from storage:", tenant_access_token)  # Log token retrieved from file
    except FileNotFoundError:
        # If the file doesn't exist, generate a new token
        tenant_access_token = get_tenantAccessToken_funct.get_tenant_access_token()
        print("Generated new tenant_access_token:", tenant_access_token)

    # Try to create a record
    try:
        response = create_record(app_base_token, base_table_id, tenant_access_token, fields_json)
        
        # Check if response indicates an invalid token
        if response.status_code == 401 or (response.json().get("code") == 99991663 or "Invalid access token" in response.json().get("msg", "")):
            print("Invalid access token or token expired, getting a new token...")
            tenant_access_token = get_tenantAccessToken_funct.get_tenant_access_token()
            print("New tenant_access_token:", tenant_access_token)
            # Try creating the record again with the new token
            response = create_record(app_base_token, base_table_id, tenant_access_token, fields_json)
        else:
            print("Record created successfully.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
    
    # Save the (potentially new) tenant_access_token to storage
    with open('tenantAccessToken_storage.txt', 'w') as file:
        file.write(tenant_access_token)

    print("Final tenant_access_token:", tenant_access_token)
    
create_record_with_checkTenantAccessToken(app_base_token, base_table_id, fields_json)
