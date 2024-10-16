import requests
import json
# method: POST
# endpoint: https://open.larksuite.com/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records

# Link base: https://csg2ej4iz2hz.sg.larksuite.com/base/HTJ6bPPPfaelL5sKDVglGHHOgCg?table=tblpgKokUDFf7cFn
# Parameters
app_base_token = "<>" # app_token là mã định danh của ứng dụng Base
table_id = "<>" # table_id là mã định danh của bảng trong Base

url = f"https://open.larksuite.com/open-apis/bitable/v1/apps/{app_base_token}/tables/{table_id}/records"

# Body: 
## Các cột cần có sẵn trong Base: NHỚ PHẢI ĐÚNG TÊN CỘT CHỨ
payload = json.dumps({
	"fields": {
		"conversation_id": "Example Text"
	}
})


# Authorization và Header
# Authorization: Giá trị của access token (dạng "Bearer access_token")
# Content-Type: "application/json; charset=utf-8"
lark_bearer_user_access_token = "<>"
headers = {
  'Authorization': f'Bearer {lark_bearer_user_access_token}',
  'Content-Type': 'application/json'
}

# Add this line to disable SSL certificate verification
requests.packages.urllib3.disable_warnings()

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.text)
