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


# Get tenant access token
tenant_access_token = get_tenantAccessToken_funct.get_tenant_access_token()
print("tenant_access_token:", tenant_access_token)

url = f"https://open.larksuite.com/open-apis/bitable/v1/apps/{app_base_token}/tables/{base_table_id}/records"
payload = json.dumps({
	"fields": {
		"Multi-select column": [
			"Option1",
			"Option2"
		],
		"conversation_id": "Example Text"
	}
})


headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {tenant_access_token}'
}


# Add this line to disable SSL certificate verification
requests.packages.urllib3.disable_warnings()
response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.text)


