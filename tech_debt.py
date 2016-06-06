import requests

import secrets

url = 'https://gigwalk.myjetbrains.com/youtrack/rest/user/login'
payload = {'login': secrets.username, 'password': secrets.password}
resp = requests.post(url, data=payload)
print resp.status_code
print resp.content
